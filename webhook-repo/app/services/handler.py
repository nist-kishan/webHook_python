# handler.py
"""Business‑logic layer – parses raw GitHub payloads and persists minimal data required by the UI."""
import logging
from datetime import datetime
from typing import Any, Dict

from app.models.event import Event
from app.utils.db import events_collection, errors

logger = logging.getLogger(__name__)


def _insert_event(evt: Event) -> None:
    """Insert an Event into MongoDB with logging and error‑handling."""
    try:
        logger.debug("✅ Inserting event: %s", evt.to_dict())
        events_collection.insert_one(evt.to_dict())
    except errors.PyMongoError as exc:
        logger.error("Failed to store event: %s", exc)


def handle_push(payload: Dict[str, Any]) -> None:
    """Handle a GitHub *push* webhook."""
    author = payload.get("pusher", {}).get("name", "unknown")
    to_branch = payload.get("ref", "refs/heads/unknown").split("/")[-1]

    evt = Event(event_type="push", author=author, to_branch=to_branch)
    _insert_event(evt)


def handle_pull_request(payload: Dict[str, Any]) -> None:
    """Handle *pull_request* and *merge* events from GitHub."""
    action = payload.get("action")
    pr = payload.get("pull_request", {})

    author = pr.get("user", {}).get("login", "unknown")
    from_branch = pr.get("head", {}).get("ref")
    to_branch = pr.get("base", {}).get("ref")

    if action == "opened":
        timestamp = pr.get("created_at")
        evt_type = "pull_request"
    elif action == "closed" and pr.get("merged"):
        timestamp = pr.get("merged_at")
        evt_type = "merge"
    else:
        logger.info("Ignoring PR action: %s", action)
        return

    evt = Event(evt_type, author, timestamp or datetime.utcnow().isoformat(), from_branch, to_branch)
    _insert_event(evt)

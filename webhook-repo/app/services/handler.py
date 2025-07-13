"""
Business‑logic layer – parses raw GitHub payloads and
persists minimal data required by the UI.
"""
from app.models.event import Event
from app.utils.db import events_collection


def handle_push(payload: dict) -> None:
    author = payload["pusher"]["name"]
    to_branch = payload["ref"].split("/")[-1]
    evt = Event("push", author, to_branch=to_branch)
    events_collection.insert_one(evt.to_dict())


def handle_pull_request(payload: dict) -> None:
    action = payload["action"]
    pr = payload["pull_request"]

    author = pr["user"]["login"]
    from_branch = pr["head"]["ref"]
    to_branch = pr["base"]["ref"]

    if action == "opened":
        timestamp = pr["created_at"]
        evt_type = "pull_request"
    elif action == "closed" and pr.get("merged"):
        timestamp = pr["merged_at"]
        evt_type = "merge"
    else:
        # Ignore other PR actions (e.g. edited, reopened)
        return

    evt = Event(evt_type, author, timestamp, from_branch, to_branch)
    events_collection.insert_one(evt.to_dict())

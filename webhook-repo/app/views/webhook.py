# webhook.py
from flask import Blueprint, request, jsonify, current_app
from werkzeug.exceptions import BadRequest

from app.services.handler import handle_push, handle_pull_request
from app.utils.db import events_collection

webhook_bp = Blueprint("webhook", __name__)


@webhook_bp.route("/webhook", methods=["POST"])
def webhook():
    try:
        event_type = request.headers.get("X-GitHub-Event")
        payload = request.get_json(force=True)
    except BadRequest as exc:
        current_app.logger.warning("Invalid JSON payload: %s", exc)
        return jsonify({"error": "Invalid JSON"}), 400

    current_app.logger.info("📬 Webhook received: %s", event_type)

    if not event_type:
        return jsonify({"error": "Missing X-GitHub-Event header"}), 400

    match event_type:
        case "ping":
            return jsonify({"msg": "Ping received"}), 200
        case "push":
            handle_push(payload)
        case "pull_request":
            handle_pull_request(payload)
        case _:
            current_app.logger.info("Unhandled GitHub event: %s", event_type)

    return jsonify({"status": "received"}), 200


@webhook_bp.route("/events", methods=["GET"])
def get_events():
    """Frontend hits this every 15 s. Return newest first for convenience."""
    data = list(events_collection.find({}, {"_id": 0}).sort("timestamp", -1))
    return jsonify(data), 200

from flask import Blueprint, request, jsonify
from app.services.handler import handle_push, handle_pull_request
from app.utils.db import events_collection

webhook_bp = Blueprint("webhook", __name__)


@webhook_bp.route("/webhook", methods=["POST"])
def webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.get_json(silent=True)

    if not payload or not event_type:
        return jsonify({"error": "Invalid payload"}), 400

    if event_type == "push":
        handle_push(payload)
    elif event_type == "pull_request":
        handle_pull_request(payload)
    else:
        # For this assignment we only care about push / PR / merge
        pass

    return jsonify({"status": "received"}), 200


@webhook_bp.route("/events", methods=["GET"])
def get_events():
    """
    Frontend hits this every 15 s.
    Return newest first for convenience.
    """
    data = list(
        events_collection.find({}, {"_id": 0}).sort("timestamp", -1)
    )
    return jsonify(data), 200

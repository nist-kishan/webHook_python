# db.py
import os
import logging
from pymongo import MongoClient, errors

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB", "github_webhooks")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "events")

logger = logging.getLogger(__name__)

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5_000)
    client.server_info()  # Trigger connection for early failure
except errors.ServerSelectionTimeoutError as exc:
    logger.error("❌  MongoDB connection failed: %s", exc)
    raise SystemExit("Cannot start without MongoDB") from exc


db = client[DB_NAME]
events_collection = db[COLLECTION_NAME]

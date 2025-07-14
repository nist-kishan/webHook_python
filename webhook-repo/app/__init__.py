# __init__.py
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import logging
import os


def create_app() -> Flask:
    load_dotenv()

    app = Flask(__name__)

    # Logging – DEBUG in dev, WARNING in prod
    log_level = logging.DEBUG if app.debug or os.getenv("FLASK_ENV") != "production" else logging.WARNING
    logging.basicConfig(level=log_level, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

    # Restrict CORS in production
    cors_origins = os.getenv("CORS_ORIGINS", "*")
    CORS(app, resources={r"/*": {"origins": cors_origins.split(",")}})

    from .views.webhook import webhook_bp

    app.register_blueprint(webhook_bp)

    return app

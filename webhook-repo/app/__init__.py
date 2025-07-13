from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()

    app = Flask(__name__)
    CORS(app)

    from .views.webhook import webhook_bp
    app.register_blueprint(webhook_bp)

    return app

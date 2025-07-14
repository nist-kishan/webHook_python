# main.py
import os
from app import create_app

PORT = int(os.getenv("PORT", 5000))

app = create_app()

if __name__ == "__main__":
    # Use waitress or gunicorn in production
    app.run(host="0.0.0.0", port=PORT, debug=app.debug)

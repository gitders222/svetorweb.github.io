# app/__init__.py

from flask import Flask
from app.routes import init_routes
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config.from_object('config.Config')

    # Initialize routes
    init_routes(app)

    # Initialize database
    db.init_app(app)

    return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Database object
db = SQLAlchemy()

# Application Factory
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Make sure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register Database
    db.init_app(app)

    with app.app_context():
        # Import Blueprints
        from .main_blueprint.routes import bp as main_blueprint_routes

        # Register Blueprints
        app.register_blueprint(main_blueprint_routes)

        # Create database tables
        db.create_all()

        return app

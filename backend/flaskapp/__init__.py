from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database object
db = SQLAlchemy()

# Application Factory
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Register Database
    db.init_app(app)

    # Import Blueprints
    from .main_blueprint.routes import bp as main_blueprint_routes

    # Register Blueprints
    app.register_blueprint(main_blueprint_routes)

    with app.app_context():
        # Create database tables
        db.create_all()

    return app

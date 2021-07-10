from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_minio import Minio
from sqlalchemy.exc import OperationalError
from time import sleep

# Database object
db = SQLAlchemy()

# Minio client object
s3 = Minio()

# Application Factory
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    # Register Database
    db.init_app(app)
    s3.init_app(app)

    # Import Blueprints
    from .main.routes import bp as main_routes
    from .storage.routes import bp as storage_routes
    from .database.routes import bp as database_routes

    # Register Blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(storage_routes)
    app.register_blueprint(database_routes)

    with app.app_context():
        # Try every 0.5 seconds to connect to the database
        # Note: Not sure if this fixes the initial connect problem or not.
        while True:
            try:
                # Create database tables
                db.create_all()
                print("Database connected")
                break
            except OperationalError:
                print("Database connection failed")
                sleep(0.5)

    return app

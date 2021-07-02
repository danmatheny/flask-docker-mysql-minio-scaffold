# Configuration variables and secrets for Flask application.  Most are set from environment variables

from os import environ

# Flask configuration
SECRET_KEY = "secret session key"

# Database configuration
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:devdbpass@mysqldb/testdb"
SQLALCHEMY_TRACK_MODIFICATIONS = False

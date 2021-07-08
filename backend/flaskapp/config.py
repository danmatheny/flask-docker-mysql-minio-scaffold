# Configuration variables and secrets for Flask application.  Most are set from environment variables

from os import environ

# Environment Variables needed:
# SESSION_KEY
# MYSQL_USER
# MYSQL_PASSWORD
# MYSQL_HOST
# MYSQL_DATABASE
# S3_URL
# S3_ACCESS_KEY
# S3_SECRET_KEY

# Flask configuration
SECRET_KEY = environ.get("SESSION_KEY")

# Database configuration
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{environ.get("MYSQL_USER")}:{environ.get("MYSQL_PASSWORD")}@{environ.get("MYSQL_HOST")}/{environ.get("MYSQL_DATABASE")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# S3 storage configuration
MINIO_ENDPOINT = environ.get("S3_URL")
MINIO_ACCESS_KEY = environ.get("S3_ACCESS_KEY")
MINIO_SECRET_KEY = environ.get("S3_SECRET_KEY")
MINIO_SECURE = False

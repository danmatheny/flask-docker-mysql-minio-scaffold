from flask import Blueprint, request, render_template, redirect, url_for
from flaskapp.database.models import User

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    # Get all users from the database
    users = User.query.all()
    return render_template("index.html", users=users)


# To view files directory from the internal MinIO S3 Storage, we create a URL rule.
# Note that we are not defining a view function associated with it, as we usually do.
# We could define one to get the file from S3 and then send that file, but having Flask fetch every image is would be very inefficient. Instead, we will just tell Nginx to proxy requests to this URL to MinIO.
# Note: The bucket and object must be publically accessible for this to work!
bp.add_url_rule("/image/<bucket_name>/<object_name>", "s3image")

from flask import Blueprint, request, render_template, redirect, url_for
from flaskapp.database.models import User

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    # Get all users from the database
    users = User.query.all()
    return render_template("index.html", users=users)

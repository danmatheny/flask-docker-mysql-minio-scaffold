from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, User

bp = Blueprint("main_blueprint", __name__)


@bp.route("/")
def index():
    # Get all users from the database
    users = User.query.all()
    return render_template("index.html", users=users)


# Create a user via query strings
@bp.route("/createuser")
def create_user():
    name = request.args.get("name")
    email = request.args.get("email")

    if name and email:
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()

    return redirect(url_for("main_blueprint.index"))


# Another test route
@bp.route("/anothertest")
def anothertest():
    return "Another test route!!!"

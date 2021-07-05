from flask import Blueprint, request, render_template, redirect, url_for
from ..models import db, User

bp = Blueprint("main_blueprint", __name__)


@bp.route("/")
def index():
    # Get all users from the database
    users = User.query.all()
    return render_template("index.html", users=users)


# Create and delete database entries
@bp.route("/editusers", methods=["GET", "POST"])
def edit_users():
    # On POST requests, process the form data and modify the database
    if request.method == "POST":
        # Create a new user
        new_user_name = request.form.get("add_name")
        new_user_email = request.form.get("add_email")
        if new_user_name and new_user_email:
            new_user = User(name=new_user_name, email=new_user_email)
            db.session.add(new_user)

        # Remove users
        user_ids_to_remove = request.form.getlist("remove")
        for id in user_ids_to_remove:
            user = User.query.get(id)
            if user:
                db.session.delete(user)

        # Commit the database session
        db.session.commit()

        # return redirect(url_for("main_blueprint.index"))
        return redirect(url_for(".index"))

    # On GET requests, display the form to modify the database
    users = User.query.all()

    return render_template("edit_users.html", users=users)

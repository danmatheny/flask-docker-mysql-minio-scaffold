from flask import Blueprint, request, render_template, redirect, url_for
from .models import db, User

bp = Blueprint("database", __name__, url_prefix="/database")

# Create and edit users in the database
@bp.route("/", methods=["GET", "POST"])
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

        return redirect(url_for("main.index"))

    # On GET requests, display the form to modify the database
    users = User.query.all()

    return render_template("edit_users.html", users=users)

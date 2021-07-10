from werkzeug.local import F
from flaskapp.storage.operations import create_public_bucket, upload_object
from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from flaskapp import s3

bp = Blueprint("storage", __name__, url_prefix="/storage")


# List all objects in the s3 storage space
@bp.route("/", methods=["GET", "POST"])
def explore_storage():
    # Request type POST
    if request.method == "POST":
        if "file" in request.files:
            # Upload file object
            file = request.files["file"]
            bucket = request.form.get("bucket")
            filename = secure_filename(file.filename)
            folder = request.form.get("folder")
            if folder:
                filename = folder + "/" + filename

            if file:
                upload_object(bucket, filename, file)

        new_bucket_name = request.form.get("new-bucket")
        if new_bucket_name:
            create_public_bucket(new_bucket_name)

        return redirect(url_for("storage.explore_storage"))

    # Request type GET
    # Create a dictionary of all objects in all buckets
    buckets = []
    for bucket in s3.connection.list_buckets():
        bucket_entry = {"bucket_name": bucket.name}

        # Get all objects in the bucket
        objects = []
        for object in s3.connection.list_objects(bucket.name, recursive=True):
            object_entry = {
                "object_name": object.object_name,
                "content_type": object.content_type,
                "size": object.size,
            }
            objects.append(object_entry)

        bucket_entry["objects"] = objects
        buckets.append(bucket_entry)

    directory_tree = {"buckets": buckets}
    return render_template("explore_storage.html", files=directory_tree)

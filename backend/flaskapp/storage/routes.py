from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
import os
from .s3 import s3

bp = Blueprint("storage", __name__, url_prefix="/storage")


# List all objects in the s3 storage space
@bp.route("/", methods=["GET", "POST"])
def explore_storage():
    if request.method == "POST":
        if "file" in request.files:
            # Upload file object
            file = request.files["file"]
            bucket = request.form.get("bucket")
            filename = secure_filename(file.filename)
            folder = request.form.get("folder")
            if folder:
                filename = folder + "/" + filename

            # seek to the end of the file to tell its size
            file.seek(0, os.SEEK_END)
            file_size = file.tell()

            # seek to its beginning, so you might save it entirely
            file.seek(0)
        try:
            s3.put_object(bucket, filename, file, file_size)
        except Exception as error:
            print("File upload failed: ", error)

        return redirect(url_for("storage.explore_storage"))

    # Create a dictionary of all objects in all buckets
    buckets = []
    for bucket in s3.list_buckets():
        bucket_entry = {"bucket_name": bucket.name}

        # Get all objects in the bucket
        objects = []
        for object in s3.list_objects(bucket.name, recursive=True):
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

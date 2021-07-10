# S3 object and bucket operations

from flaskapp import s3
import os
import json


def upload_object(bucket, filename, file):
    # Find file size
    # seek to the end of the file to tell its size
    file.seek(0, os.SEEK_END)
    file_size = file.tell()

    # seek to its beginning, so you might save it entirely
    file.seek(0)

    # Upload to s3
    try:
        s3.connection.put_object(bucket, filename, file, file_size)
    except Exception as error:
        print("File upload failed: ", error)


def create_public_bucket(bucket_name):
    # Create the bucket in s3
    try:
        s3.connection.make_bucket(bucket_name)
    except Exception as error:
        print("Bucket creation failed", error)

    if s3.connection.bucket_exists(bucket_name):
        # Create anonymous read-only policy for the bucket
        policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": ["s3:GetBucketLocation", "s3:ListBucket"],
                    "Resource": f"arn:aws:s3:::{bucket_name}",
                },
                {
                    "Effect": "Allow",
                    "Principal": {"AWS": "*"},
                    "Action": "s3:GetObject",
                    "Resource": f"arn:aws:s3:::{bucket_name}/*",
                },
            ],
        }
        s3.connection.set_bucket_policy(bucket_name, json.dumps(policy))

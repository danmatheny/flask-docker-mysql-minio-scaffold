from minio import Minio

s3 = Minio("minio:9000", access_key="admin", secret_key="devstoragepass", secure=False)

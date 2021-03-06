# flask-docker-mysql-minio-scaffold

This project implements a full-stack web application combining Flask, MySQL, and MinIO in a Docker Compose stack.

The application itself does almost nothing. This is really about seeing how multiple applications can be combined using Docker, and also to provide an application scaffolding that can be modified to use with real applications.

## Building and running development

In the project directory:

    docker-compose -f docker-compose-dev.yaml --env-file .env-dev up --build

Note: Repeated builds will generate a lot of "dangling" images, which occur when a build replaces a previous build with the same tag. Clear them up with

    docker rmi $(docker images -f "dangling=true" -q)

## Building and running production

The production files are given the default names, so the command to run the stack is much simpler:

    docker-compose up -d

You can also be more verbose:

    docker-compose -f docker-compose.yaml --env-file .env up -d

(Here the `-d` option is to run in "detached" mode, so the logs will not be displayed to the console.)

However, the production stack does not build and run the local container images, but instead pulls them from the container repository (in this case Docker Hub).

To build the images, using a multi-architecture build (x86 64-bit and ARM 64-bit), first create a builder:

    docker buildx create --name multiarch-builder --use

Then build and push to the repository (must be logged in with `docker login`):

    docker buildx build \
        -t danmatheny/fullstack-flaskapp-scaffold \
        --platform linux/amd64,linux/arm64 \
        --push \
        backend

and

    docker buildx build \
        -t danmatheny/fullstack-flaskapp-scaffold-nginx \
        --platform linux/amd64,linux/arm64 \
        --push \
        --file ./nginx/Dockerfile \
        .

This builds two images, the main Flask app image (build context in the `backend` folder) and the custom Nginx reverse proxy (build context in the project root (i.e. `.`) directory).

Note: The build context for the Nginx image must include the `backend` folder because the `Dockerfile` will copy the static files from the Flask application to the Nginx container. Since we have the `Dockerfile` for the Nginx image in the `nginx` directory, we need to specify a path to the `Dockerfile`.

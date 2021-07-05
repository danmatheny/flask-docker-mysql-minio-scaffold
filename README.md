# flask-docker-mysql-minio-scaffold

This project implements a full-stack web application combining Flask, MySQL, and MinIO in a Docker Compose stack.

The application itself does almost nothing. This is really about seeing how multiple applications can be combined using Docker, and also to provide an application scaffolding that can be modified to use with real applications.

## Building and running development

In the project directory:

    docker-compose -f docker-compose-dev.yaml --env-file .env-dev up --build

Note: Repeated builds will generate a lot of "dangling" images, which occur when a build replaces a previous build with the same tag. Clear them up with

    docker rmi $(docker images -f "dangling=true" -q)

## Running production

The production files are given the default names, so the command to run the stack is much simpler:

    docker-compose up

You can also be more verbose:

    docker-compose -f docker-compose.yaml --env-file .env up

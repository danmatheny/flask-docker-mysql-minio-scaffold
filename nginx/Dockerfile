FROM nginx

# Copy the static files from the backend Flask app to the Nginx container
COPY ./backend/flaskapp/static /static

# Replace config with our own nginx.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
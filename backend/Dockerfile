# syntax=docker/dockerfile:1

FROM python:3.9-slim

RUN apt-get clean \
  && apt-get -y update \
  && apt-get -y install gcc

RUN pip install wheel

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=flaskapp
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["uwsgi", "uwsgi.ini"]

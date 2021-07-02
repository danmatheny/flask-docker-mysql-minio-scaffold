# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=flaskapp
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["flask", "run"]
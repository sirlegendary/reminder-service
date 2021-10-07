# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# set environment variables
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

# install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["python", "app.py"]
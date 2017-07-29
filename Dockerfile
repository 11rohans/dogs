FROM python:3.6.1
MAINTAINER Rohan Singh (11rohans@gmail.com)

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 5000

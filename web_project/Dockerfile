FROM python:3.11
LABEL maintainer="goktugatahan"

ENV PYTHONUNBUFFERED 1

COPY ./web/requirements.txt /web/requirements.txt
RUN pip install -r /web/requirements.txt

WORKDIR /web
COPY ./web /web

EXPOSE 8000


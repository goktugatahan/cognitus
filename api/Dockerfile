FROM python:3.11
LABEL maintainer="goktugatahan"

ENV PYTHONUNBUFFERED 1

COPY ./dataapp/requirements.txt /dataapp/requirements.txt
COPY ./dataapp /dataapp
WORKDIR /dataapp
EXPOSE 8081


RUN pip install -r /dataapp/requirements.txt
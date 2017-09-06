FROM python:3.6

LABEL maintainer="Paulo Matos <paulo@matos-sorge.com>"

ADD . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=.:$PYTHONPATH
ENV FLASK_APP=mseye
CMD flask run --host=0.0.0.0

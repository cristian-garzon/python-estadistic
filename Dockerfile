# first step: create a engine
FROM python:3.10

#create a dir
COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN python main.py



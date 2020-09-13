FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y wait-for-it

RUN mkdir /code

WORKDIR /code
COPY emenu/requirements.txt /code/
RUN pip install -r requirements.txt

COPY emenu/ /code/
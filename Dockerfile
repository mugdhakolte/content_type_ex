FROM --platform=linux/amd64 python:3.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /content_type

# install dependencies
RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y libpq-dev

COPY requirements.txt /content_type/

RUN pip install -r requirements.txt
COPY . /content_type/
COPY .env /content_type/.env
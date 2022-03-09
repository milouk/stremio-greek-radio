FROM tiangolo/uvicorn-gunicorn-fastapi:latest-2021-06-09

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app /app

EXPOSE 8000

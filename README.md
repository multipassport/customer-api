# Customer API

A simple application which makes REST requests to the database

## Launch

Make sure you have Docker compose installed. Copy the contents of `.env.example` to the `.env` file

```sh
cp .env.example .env
```

Run project with docker compose

```sh
docker compose up --build -d
```

## Running tests

```sh
docker compose -f docker-compose-test.yaml up --build
```

## Dockerhub image location

https://hub.docker.com/repository/docker/multipassport/customer_api/general

# FastAPI + Postgres: Proof of Concept

## Overview

A simple proof of concept using:
* [FastAPI ](https://fastapi.tiangolo.com/): Python API web framework;
* [SQLAlchemy](https://pypi.org/project/FastAPI-SQLAlchemy/): Python SQL toolkit and ORM;
* [Psycopg](https://pypi.org/project/psycopg2/): Python PostgreSQL database adapter;
( [Alembic](https://alembic.sqlalchemy.org/en/latest/): Database migration tool for Python SQLAlechemy;
* [Uvicorn](https://www.uvicorn.org/): ASGI server implementation;

## Migrations

All migration commmands should be run inside the `alembic` folder. 

To create a new migration, do:
```
alembic revision -m "<describe your migration here>"

```
To run all migrations, do:
```
alembic upgrade head
```

To roll back the last migration, do:
```
alembic downgrade -1
```

## Run

### Locally

To laucnch the app locally with reloading on code changes, run:
```
uvicorn api.main:app --reload
```



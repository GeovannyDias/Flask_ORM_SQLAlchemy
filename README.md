# Flask - ORM SQLAlchemy
Flask - ORM with SQLAlchemy


## Commands

```
virtualenv -p python3 env
.\env\Scripts\activate
pip list
python -m pip install --upgrade pip

pip install flask==1.1.4  → Se Utiliza esta version para solventar problmas de migraciones (flask-script)
pip install flask

pip install flask-sqlalchemy
pip install psycopg2
pip install flask-migrate==2.1.1 → Se utiliza esta versión por temas de compatibilidad
pip install flask-migrate
pip install flask-script

Make Directory:

md src/app


--------------------------------------------------------------------------------

pip install flask-mysqldb → Forma de instalar MySql desde la documentación

pip install flask flask_mysqldb

Make Directory:
md src
pip freeze > requirements.txt


```

## Install Requirements

```
Tools used in this part:

PostgreSQL
Psycopg2 - a Python adapter for Postgres
Flask-SQLAlchemy - Flask extension that provides SQLAlchemy support
Flask-Migrate - extension that supports SQLAlchemy database migrations via Alembic
Flask-Script - which was used before by Flask-Migrate. In order to use it

```


## Estructura de un proyecto Flask. Blueprints

* **https://j2logo.com/tutorial-flask-leccion-6-estructura-proyecto-flask-blueprints/*

## Setting up Postgres → *

* **https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/#install-requirements**


## Extension

* **https://flask-sqlalchemy.palletsprojects.com/en/2.x/**
* **https://flask-migrate.readthedocs.io/en/latest/**
* **https://flask-script.readthedocs.io/en/latest/**


## DB Reference

* **https://codigosql.top/sql-server/llaves-primarias-y-foraneas-en-sql-server/**

## Error

* **https://stackoverflow.com/questions/67538056/flask-script-from-flask-compat-import-text-type-modulenotfounderror-no-module**


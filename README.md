# database-version-control

## Description

Repository for managing changes to the database schema using [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#).

## Repo structure

- `alembic.ini`: Alembic configuration file
- `alembic/versions`: Alembic migration scripts
- `models.py`: SQLAlchemy declarative models for tables to create the initial/baseline version for the database.

## Usage

### Migration 

Change directroy to the proper location, e.g. if migriaon is to be applied to the aiven database, change directory to `aiven`:

```
alembic_src/aiven_postgres
```

Create new migration scripts by running the following command (see [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html#:~:text=Create%20a%20Migration%20Script%C2%B6)):

```
alembic revision -m "Some message"
```

populate the `upgrade` and `downgrade` functions in the newly created migration script.

To apply the migration scripts to the database, run:

```
alembic upgrade head
```

### Relative migration

To apply a migration script relative to the current revision, run:

```
alembic upgrade +1
```

## Stamp database version

To stamp the database version (i.e. set the version of databse manually), run:

```
alemibc stamp <revision>
```

`<reviison>` can be found at the beggining of each migration script or on the name of the migration script file.

## Downgrade

To downgrade the database to a specific version, run:

```
alembic downgrade <revision>
```

`<reviison>` can be found at the beggining of each migration script or on the name of the migration script file.

## Create table in models.py (version 0)

To create a table in `models.py` (i.e. create the initial version of the database), run:

```
alembic revision --autogenerate
```


# Structure of the migration scripts

This repo manages migration files for multiple databases (e.g. postgres hosted on aiven, neon, etc.). Each database has its own directory under `alembic_src`. Each directory has the following structure:

- `alembic.ini`: Alembic configuration file
- `alembic/versions`: Alembic migration scripts
- `models.py`: SQLAlchemy declarative models for tables to create the initial/baseline version for the database.
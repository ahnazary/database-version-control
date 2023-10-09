# database-version-control

## Description

Repository for managing changes to the database schema using [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html#).

## Repo structure

- `alembic.ini`: Alembic configuration file
- `alembic/versions`: Alembic migration scripts
- `models.py`: SQLAlchemy declarative models for tables to create the initial/baseline version for the database.

## Usage

### Migration 

Create new migration scripts by running(see [here](https://alembic.sqlalchemy.org/en/latest/tutorial.html#:~:text=Create%20a%20Migration%20Script%C2%B6)):

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
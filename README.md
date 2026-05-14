# mflsoildata_orm

ORM for the Soil Platform v6 database (PostgreSQL + PostGIS).

## Requirements

- Python >= 3.10
- PostgreSQL with PostGIS

## Installation

```bash
pip install -e .
```

## Environment

Set the database connection string with `DATABASE_URL`.

Example:

```text
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/soil_platform
```

## Usage

```python
from mflsoildata_orm.services.project_service import ProjectService
from mflsoildata_orm.schemas.project_schema import ProjectCreate

service = ProjectService()
project = service.create(ProjectCreate(code="CLIMALOCA", name="Clima LoCa"))
print(project.id)
```

## Migrations

Migrations are provided in the package. You can run them programmatically:

```python
from mflsoildata_orm.migrations import upgrade, current

upgrade()
current()
```

To create the database schema locally you can either run alembic or use the package helper.

1) Run Alembic upgrade (recommended if you want migration history):

```powershell
setx DATABASE_URL "postgresql://postgres:postgres@localhost:5432/soil_platform"
python -m pip install -e .
alembic -c src/mflsoildata_orm/alembic.ini upgrade head
```

2) Quick create (not tracked by alembic history):

```powershell
setx DATABASE_URL "postgresql://postgres:postgres@localhost:5432/soil_platform"
python -m pip install -e .
python -c "from mflsoildata_orm.database.base import create_tables; create_tables()"
```

If you run the packaged alembic helper programmatically, it will also use `DATABASE_URL`.

Note: This repository includes a baseline migration (src/mflsoildata_orm/migrations/versions/0001_baseline.py)
that calls `Base.metadata.create_all()` during upgrade; it's a safe way to bootstrap the schema but you
may prefer to generate proper autogenerate revisions for long-term maintenance.

## Publishing

Build and publish to PyPI:

```powershell
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
```

You'll need PyPI credentials or a repository URL for private indexes. Bump the version in `pyproject.toml` before publishing.


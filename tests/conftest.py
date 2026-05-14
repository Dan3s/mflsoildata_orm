import os

import pytest

# Default tests to an in-memory SQLite DB unless DATABASE_URL already set
os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///:memory:")

from mflsoildata_orm.database import SessionLocal, engine
from mflsoildata_orm.database.base import Base

# Import only the models used by tests to avoid PostGIS/Geometry issues
from mflsoildata_orm.models import (
    Project,
    Unit,
    Method,
    Lab,
    Variable,
    SampleType,
    Sample,
    SampleAttribute,
)


@pytest.fixture()
def db_session():
    # Create only the tables needed for the unit tests
    # If running tests on SQLite, provide a small shim so JSONB columns compile
    # as JSON (SQLite doesn't have JSONB). This allows create_all to succeed.
    if engine.dialect.name == "sqlite":
        try:
            from sqlalchemy.dialects.sqlite.base import SQLiteTypeCompiler

            SQLiteTypeCompiler.visit_JSONB = SQLiteTypeCompiler.visit_JSON
        except Exception:
            pass

    # Exclude Project because it uses JSONB which SQLite cannot compile
    tables = [
        Unit.__table__,
        Method.__table__,
        Lab.__table__,
        Variable.__table__,
        SampleType.__table__,
        Sample.__table__,
        SampleAttribute.__table__,
    ]
    Base.metadata.create_all(bind=engine, tables=tables)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine, tables=tables)

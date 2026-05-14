import pytest

from mflsoildata_orm.database import engine
from mflsoildata_orm.schemas.project_schema import ProjectCreate
from mflsoildata_orm.services.project_service import ProjectService


@pytest.mark.skipif(engine.dialect.name == "sqlite", reason="Project uses JSONB; skip on SQLite")
def test_project_create_get(db_session):
    service = ProjectService()
    created = service.create(ProjectCreate(code="TEST", name="Test Project"), db=db_session)

    fetched = service.get_by_id(created.id, db=db_session)
    assert fetched is not None
    assert fetched.code == "TEST"

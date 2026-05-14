from mflsoildata_orm.services.lab_service import LabService
from mflsoildata_orm.schemas.lab_schema import LabCreate


def test_create_and_get_lab(db_session):
    svc = LabService(db_session)
    dto = LabCreate(name="Test Lab")
    created = svc.create(dto)
    fetched = svc.get_by_id(created.id)
    assert fetched.name == "Test Lab"

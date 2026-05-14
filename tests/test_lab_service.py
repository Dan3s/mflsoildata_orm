from mflsoildata_orm.services.lab_service import LabService
from mflsoildata_orm.schemas.lab_schema import LabCreate


def test_create_and_get_lab(db_session):
    svc = LabService()
    dto = LabCreate(lab_code="LAB1", name="Test Lab")
    created = svc.create(dto, db=db_session)
    fetched = svc.get_by_id(created.id, db=db_session)
    assert fetched.name == "Test Lab"

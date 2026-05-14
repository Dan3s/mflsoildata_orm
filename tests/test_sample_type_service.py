from mflsoildata_orm.services.sample_type_service import SampleTypeService
from mflsoildata_orm.schemas.sample_type_schema import SampleTypeCreate


def test_create_and_get_sample_type(db_session):
    svc = SampleTypeService()
    dto = SampleTypeCreate(sample_type_code="SOIL", name="Soil")
    created = svc.create(dto, db=db_session)
    fetched = svc.get_by_id(created.id, db=db_session)
    assert fetched.name == "Soil"

from mflsoildata_orm.services.sample_type_service import SampleTypeService
from mflsoildata_orm.schemas.sample_type_schema import SampleTypeCreate


def test_create_and_get_sample_type(db_session):
    svc = SampleTypeService(db_session)
    dto = SampleTypeCreate(name="Soil")
    created = svc.create(dto)
    fetched = svc.get_by_id(created.id)
    assert fetched.name == "Soil"

from mflsoildata_orm.services.sample_attribute_service import SampleAttributeService
from mflsoildata_orm.services.unit_service import UnitService
from mflsoildata_orm.schemas.sample_attribute_schema import SampleAttributeCreate
from mflsoildata_orm.schemas.unit_schema import UnitCreate


def test_create_and_get_sample_attribute(db_session):
    us = UnitService(db_session)
    u = us.create(UnitCreate(name="g/kg"))

    svc = SampleAttributeService(db_session)
    dto = SampleAttributeCreate(name="OrganicMatter", unit_id=u.id)
    created = svc.create(dto)
    fetched = svc.get_by_id(created.id)
    assert fetched.name == "OrganicMatter"

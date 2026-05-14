from mflsoildata_orm.services.sample_attribute_service import SampleAttributeService
from mflsoildata_orm.services.unit_service import UnitService
from mflsoildata_orm.schemas.sample_attribute_schema import SampleAttributeCreate
from mflsoildata_orm.schemas.unit_schema import UnitCreate


def test_create_and_get_sample_attribute(db_session):
    us = UnitService()
    u = us.create(UnitCreate(unit_code="GKG", symbol="g/kg"), db=db_session)

    svc = SampleAttributeService()
    dto = SampleAttributeCreate(
        sample_attribute_code="OM",
        name="OrganicMatter",
        value_type="numeric",
        default_unit_id=u.id,
    )
    created = svc.create(dto, db=db_session)
    fetched = svc.get_by_id(created.id, db=db_session)
    assert fetched.name == "OrganicMatter"

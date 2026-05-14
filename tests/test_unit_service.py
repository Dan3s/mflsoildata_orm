from mflsoildata_orm.schemas.unit_schema import UnitCreate
from mflsoildata_orm.services.unit_service import UnitService


def test_unit_create_get(db_session):
    service = UnitService()
    created = service.create(UnitCreate(unit_code="MGKG", symbol="mg/kg"), db=db_session)

    fetched = service.get_by_id(created.id, db=db_session)
    assert fetched is not None
    assert fetched.unit_code == "MGKG"

from mflsoildata_orm.services.variable_service import VariableService
from mflsoildata_orm.schemas.variable_schema import VariableCreate


def test_create_and_get_variable(db_session):
    svc = VariableService(db_session)
    dto = VariableCreate(name="pH", unit_id=None)
    created = svc.create(dto)
    fetched = svc.get_by_id(created.id)
    assert fetched.name == "pH"

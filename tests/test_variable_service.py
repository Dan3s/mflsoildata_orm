from mflsoildata_orm.services.variable_service import VariableService
from mflsoildata_orm.schemas.variable_schema import VariableCreate


def test_create_and_get_variable(db_session):
    svc = VariableService()
    dto = VariableCreate(
        variable_code="PH",
        name="pH",
        domain="soil",
        value_type="numeric",
    )
    created = svc.create(dto, db=db_session)
    fetched = svc.get_by_id(created.id, db=db_session)
    assert fetched.name == "pH"

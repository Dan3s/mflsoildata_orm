from mflsoildata_orm.services.method_service import MethodService
from mflsoildata_orm.schemas.method_schema import MethodCreate, MethodRead


def test_create_and_get_method(db_session):
    svc = MethodService()
    dto = MethodCreate(method_code="METH1", name="Test method")
    created = svc.create(dto, db=db_session)
    fetched = svc.get_by_id(created.id, db=db_session)
    assert fetched.name == "Test method"


def test_list_methods(db_session):
    svc = MethodService()
    dto1 = MethodCreate(method_code="M1", name="M1")
    dto2 = MethodCreate(method_code="M2", name="M2")
    svc.create(dto1, db=db_session)
    svc.create(dto2, db=db_session)
    items = svc.get_all(db=db_session)
    assert len(items) >= 2

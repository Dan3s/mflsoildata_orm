from mflsoildata_orm.services.method_service import MethodService
from mflsoildata_orm.schemas.method_schema import MethodCreate, MethodRead


def test_create_and_get_method(db_session):
    svc = MethodService(db_session)
    dto = MethodCreate(name="Test method")
    created = svc.create(dto)
    fetched = svc.get_by_id(created.id)
    assert fetched.name == "Test method"


def test_list_methods(db_session):
    svc = MethodService(db_session)
    dto1 = MethodCreate(name="M1")
    dto2 = MethodCreate(name="M2")
    svc.create(dto1)
    svc.create(dto2)
    items = svc.list()
    assert len(items) >= 2

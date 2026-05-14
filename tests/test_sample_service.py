from mflsoildata_orm.services.sample_service import SampleService
from mflsoildata_orm.services.sample_type_service import SampleTypeService
from mflsoildata_orm.schemas.sample_schema import SampleCreate
from mflsoildata_orm.schemas.sample_type_schema import SampleTypeCreate


def test_create_and_get_sample(db_session):
    sts = SampleTypeService(db_session)
    st = sts.create(SampleTypeCreate(name="Soil"))

    svc = SampleService(db_session)
    dto = SampleCreate(sample_type_id=st.id)
    created = svc.create(dto)
    fetched = svc.get_by_id(created.id)
    assert fetched.sample_type_id == st.id

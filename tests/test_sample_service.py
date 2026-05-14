from mflsoildata_orm.services.sample_service import SampleService
from mflsoildata_orm.services.sample_type_service import SampleTypeService
from mflsoildata_orm.schemas.sample_schema import SampleCreate
from mflsoildata_orm.schemas.sample_type_schema import SampleTypeCreate


def test_create_and_get_sample(db_session):
    sts = SampleTypeService()
    st = sts.create(SampleTypeCreate(sample_type_code="SOIL", name="Soil"), db=db_session)

    svc = SampleService()
    dto = SampleCreate(sample_type_id=st.id, sample_code="S1")
    created = svc.create(dto, db=db_session)
    fetched = svc.get_by_id(created.id, db=db_session)
    assert fetched.sample_type_id == st.id

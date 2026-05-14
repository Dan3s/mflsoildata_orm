from sqlalchemy.orm import Session

from ..models import Sample
from ..schemas.sample_schema import SampleCreate, SampleRead, SampleUpdate
from ..validations.sample_validation import SampleValidator
from .base_service import BaseService


class SampleService(BaseService[Sample, SampleCreate, SampleRead, SampleUpdate]):
    def __init__(self) -> None:
        super().__init__(Sample, SampleCreate, SampleRead, SampleUpdate)

    def _validate_create(self, obj_in: SampleCreate, db: Session) -> None:
        SampleValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SampleValidator.update_validate(db, obj_in, obj_id)

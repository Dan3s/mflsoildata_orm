from sqlalchemy.orm import Session

from ..models import SampleType
from ..schemas.sample_type_schema import SampleTypeCreate, SampleTypeRead, SampleTypeUpdate
from ..validations.sample_type_validation import SampleTypeValidator
from .base_service import BaseService


class SampleTypeService(
    BaseService[SampleType, SampleTypeCreate, SampleTypeRead, SampleTypeUpdate]
):
    def __init__(self) -> None:
        super().__init__(SampleType, SampleTypeCreate, SampleTypeRead, SampleTypeUpdate)

    def _validate_create(self, obj_in: SampleTypeCreate, db: Session) -> None:
        SampleTypeValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SampleTypeValidator.update_validate(db, obj_in, obj_id)

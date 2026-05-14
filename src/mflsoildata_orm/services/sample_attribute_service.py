from sqlalchemy.orm import Session

from ..models import SampleAttribute
from ..schemas.sample_attribute_schema import (
    SampleAttributeCreate,
    SampleAttributeRead,
    SampleAttributeUpdate,
)
from ..validations.sample_attribute_validation import SampleAttributeValidator
from .base_service import BaseService


class SampleAttributeService(
    BaseService[SampleAttribute, SampleAttributeCreate, SampleAttributeRead, SampleAttributeUpdate]
):
    def __init__(self) -> None:
        super().__init__(
            SampleAttribute, SampleAttributeCreate, SampleAttributeRead, SampleAttributeUpdate
        )

    def _validate_create(self, obj_in: SampleAttributeCreate, db: Session) -> None:
        SampleAttributeValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SampleAttributeValidator.update_validate(db, obj_in, obj_id)

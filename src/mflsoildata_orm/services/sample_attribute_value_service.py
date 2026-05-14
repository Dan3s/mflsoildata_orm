from sqlalchemy.orm import Session

from ..models import SampleAttributeValue
from ..schemas.sample_attribute_value_schema import (
    SampleAttributeValueCreate,
    SampleAttributeValueRead,
    SampleAttributeValueUpdate,
)
from ..validations.sample_attribute_value_validation import SampleAttributeValueValidator
from .base_service import BaseService


class SampleAttributeValueService(
    BaseService[
        SampleAttributeValue,
        SampleAttributeValueCreate,
        SampleAttributeValueRead,
        SampleAttributeValueUpdate,
    ]
):
    def __init__(self) -> None:
        super().__init__(
            SampleAttributeValue,
            SampleAttributeValueCreate,
            SampleAttributeValueRead,
            SampleAttributeValueUpdate,
        )

    def _validate_create(self, obj_in: SampleAttributeValueCreate, db: Session) -> None:
        SampleAttributeValueValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SampleAttributeValueValidator.update_validate(db, obj_in, obj_id)

from sqlalchemy.orm import Session

from ..models import SoilProfileAttributeValue
from ..schemas.soil_profile_attribute_value_schema import (
    SoilProfileAttributeValueCreate,
    SoilProfileAttributeValueRead,
    SoilProfileAttributeValueUpdate,
)
from ..validations.soil_profile_attribute_value_validation import (
    SoilProfileAttributeValueValidator,
)
from .base_service import BaseService


class SoilProfileAttributeValueService(
    BaseService[
        SoilProfileAttributeValue,
        SoilProfileAttributeValueCreate,
        SoilProfileAttributeValueRead,
        SoilProfileAttributeValueUpdate,
    ]
):
    def __init__(self) -> None:
        super().__init__(
            SoilProfileAttributeValue,
            SoilProfileAttributeValueCreate,
            SoilProfileAttributeValueRead,
            SoilProfileAttributeValueUpdate,
        )

    def _validate_create(self, obj_in: SoilProfileAttributeValueCreate, db: Session) -> None:
        SoilProfileAttributeValueValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SoilProfileAttributeValueValidator.update_validate(db, obj_in, obj_id)

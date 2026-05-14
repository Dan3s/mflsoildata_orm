from sqlalchemy.orm import Session

from ..models import SoilProfileAttribute
from ..schemas.soil_profile_attribute_schema import (
    SoilProfileAttributeCreate,
    SoilProfileAttributeRead,
    SoilProfileAttributeUpdate,
)
from ..validations.soil_profile_attribute_validation import SoilProfileAttributeValidator
from .base_service import BaseService


class SoilProfileAttributeService(
    BaseService[
        SoilProfileAttribute,
        SoilProfileAttributeCreate,
        SoilProfileAttributeRead,
        SoilProfileAttributeUpdate,
    ]
):
    def __init__(self) -> None:
        super().__init__(
            SoilProfileAttribute,
            SoilProfileAttributeCreate,
            SoilProfileAttributeRead,
            SoilProfileAttributeUpdate,
        )

    def _validate_create(self, obj_in: SoilProfileAttributeCreate, db: Session) -> None:
        SoilProfileAttributeValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SoilProfileAttributeValidator.update_validate(db, obj_in, obj_id)

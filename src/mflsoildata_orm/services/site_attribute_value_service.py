from sqlalchemy.orm import Session

from ..models import SiteAttributeValue
from ..schemas.site_attribute_value_schema import (
    SiteAttributeValueCreate,
    SiteAttributeValueRead,
    SiteAttributeValueUpdate,
)
from ..validations.site_attribute_value_validation import SiteAttributeValueValidator
from .base_service import BaseService


class SiteAttributeValueService(
    BaseService[
        SiteAttributeValue,
        SiteAttributeValueCreate,
        SiteAttributeValueRead,
        SiteAttributeValueUpdate,
    ]
):
    def __init__(self) -> None:
        super().__init__(
            SiteAttributeValue,
            SiteAttributeValueCreate,
            SiteAttributeValueRead,
            SiteAttributeValueUpdate,
        )

    def _validate_create(self, obj_in: SiteAttributeValueCreate, db: Session) -> None:
        SiteAttributeValueValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SiteAttributeValueValidator.update_validate(db, obj_in, obj_id)

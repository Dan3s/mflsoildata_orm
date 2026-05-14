from sqlalchemy.orm import Session

from ..models import SiteAttribute
from ..schemas.site_attribute_schema import SiteAttributeCreate, SiteAttributeRead, SiteAttributeUpdate
from ..validations.site_attribute_validation import SiteAttributeValidator
from .base_service import BaseService


class SiteAttributeService(
    BaseService[SiteAttribute, SiteAttributeCreate, SiteAttributeRead, SiteAttributeUpdate]
):
    def __init__(self) -> None:
        super().__init__(SiteAttribute, SiteAttributeCreate, SiteAttributeRead, SiteAttributeUpdate)

    def _validate_create(self, obj_in: SiteAttributeCreate, db: Session) -> None:
        SiteAttributeValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SiteAttributeValidator.update_validate(db, obj_in, obj_id)

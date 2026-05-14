from sqlalchemy.orm import Session

from ..schemas.site_attribute_value_schema import SiteAttributeValueCreate
from .base import require_value


class SiteAttributeValueValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SiteAttributeValueCreate) -> None:
        require_value(obj_in.site_id, "site_id")
        require_value(obj_in.site_attribute_id, "site_attribute_id")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "site_id" in obj_in:
            require_value(obj_in["site_id"], "site_id")
        if "site_attribute_id" in obj_in:
            require_value(obj_in["site_attribute_id"], "site_attribute_id")

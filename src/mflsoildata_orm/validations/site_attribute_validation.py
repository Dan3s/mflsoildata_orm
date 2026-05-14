from sqlalchemy.orm import Session

from ..models import SiteAttribute
from ..schemas.site_attribute_schema import SiteAttributeCreate
from .base import require_value, validate_unique


class SiteAttributeValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SiteAttributeCreate) -> None:
        require_value(obj_in.site_attribute_code, "site_attribute_code")
        require_value(obj_in.name, "name")
        require_value(obj_in.value_type, "value_type")
        validate_unique(
            db, SiteAttribute, "site_attribute_code", obj_in.site_attribute_code
        )

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "site_attribute_code" in obj_in:
            require_value(obj_in["site_attribute_code"], "site_attribute_code")
            validate_unique(
                db,
                SiteAttribute,
                "site_attribute_code",
                obj_in["site_attribute_code"],
                exclude_id=obj_id,
            )
        if "name" in obj_in:
            require_value(obj_in["name"], "name")
        if "value_type" in obj_in:
            require_value(obj_in["value_type"], "value_type")

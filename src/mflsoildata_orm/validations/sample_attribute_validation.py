from sqlalchemy.orm import Session

from ..models import SampleAttribute
from ..schemas.sample_attribute_schema import SampleAttributeCreate
from .base import require_value, validate_unique


class SampleAttributeValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SampleAttributeCreate) -> None:
        require_value(obj_in.sample_attribute_code, "sample_attribute_code")
        require_value(obj_in.name, "name")
        require_value(obj_in.value_type, "value_type")
        validate_unique(
            db, SampleAttribute, "sample_attribute_code", obj_in.sample_attribute_code
        )

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "sample_attribute_code" in obj_in:
            require_value(obj_in["sample_attribute_code"], "sample_attribute_code")
            validate_unique(
                db,
                SampleAttribute,
                "sample_attribute_code",
                obj_in["sample_attribute_code"],
                exclude_id=obj_id,
            )
        if "name" in obj_in:
            require_value(obj_in["name"], "name")
        if "value_type" in obj_in:
            require_value(obj_in["value_type"], "value_type")

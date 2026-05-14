from sqlalchemy.orm import Session

from ..schemas.sample_attribute_value_schema import SampleAttributeValueCreate
from .base import require_value


class SampleAttributeValueValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SampleAttributeValueCreate) -> None:
        require_value(obj_in.sample_id, "sample_id")
        require_value(obj_in.sample_attribute_id, "sample_attribute_id")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "sample_id" in obj_in:
            require_value(obj_in["sample_id"], "sample_id")
        if "sample_attribute_id" in obj_in:
            require_value(obj_in["sample_attribute_id"], "sample_attribute_id")

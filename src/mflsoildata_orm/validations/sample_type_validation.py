from sqlalchemy.orm import Session

from ..models import SampleType
from ..schemas.sample_type_schema import SampleTypeCreate
from .base import require_value, validate_unique


class SampleTypeValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SampleTypeCreate) -> None:
        require_value(obj_in.sample_type_code, "sample_type_code")
        require_value(obj_in.name, "name")
        validate_unique(db, SampleType, "sample_type_code", obj_in.sample_type_code)

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "sample_type_code" in obj_in:
            require_value(obj_in["sample_type_code"], "sample_type_code")
            validate_unique(
                db,
                SampleType,
                "sample_type_code",
                obj_in["sample_type_code"],
                exclude_id=obj_id,
            )
        if "name" in obj_in:
            require_value(obj_in["name"], "name")

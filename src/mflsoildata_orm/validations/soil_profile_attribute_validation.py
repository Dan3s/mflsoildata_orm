from sqlalchemy.orm import Session

from ..models import SoilProfileAttribute
from ..schemas.soil_profile_attribute_schema import SoilProfileAttributeCreate
from .base import require_value, validate_unique


class SoilProfileAttributeValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SoilProfileAttributeCreate) -> None:
        require_value(obj_in.soil_profile_attribute_code, "soil_profile_attribute_code")
        require_value(obj_in.name, "name")
        require_value(obj_in.value_type, "value_type")
        validate_unique(
            db,
            SoilProfileAttribute,
            "soil_profile_attribute_code",
            obj_in.soil_profile_attribute_code,
        )

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "soil_profile_attribute_code" in obj_in:
            require_value(
                obj_in["soil_profile_attribute_code"], "soil_profile_attribute_code"
            )
            validate_unique(
                db,
                SoilProfileAttribute,
                "soil_profile_attribute_code",
                obj_in["soil_profile_attribute_code"],
                exclude_id=obj_id,
            )
        if "name" in obj_in:
            require_value(obj_in["name"], "name")
        if "value_type" in obj_in:
            require_value(obj_in["value_type"], "value_type")

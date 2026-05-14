from sqlalchemy.orm import Session

from ..schemas.soil_profile_attribute_value_schema import SoilProfileAttributeValueCreate
from .base import require_value


class SoilProfileAttributeValueValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SoilProfileAttributeValueCreate) -> None:
        require_value(obj_in.soil_profile_id, "soil_profile_id")
        require_value(obj_in.soil_profile_attribute_id, "soil_profile_attribute_id")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "soil_profile_id" in obj_in:
            require_value(obj_in["soil_profile_id"], "soil_profile_id")
        if "soil_profile_attribute_id" in obj_in:
            require_value(
                obj_in["soil_profile_attribute_id"], "soil_profile_attribute_id"
            )

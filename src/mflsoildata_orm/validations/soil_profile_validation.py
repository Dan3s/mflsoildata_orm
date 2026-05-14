from sqlalchemy.orm import Session

from ..schemas.soil_profile_schema import SoilProfileCreate
from .base import require_value


class SoilProfileValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SoilProfileCreate) -> None:
        require_value(obj_in.project_id, "project_id")
        require_value(obj_in.profile_code, "profile_code")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "project_id" in obj_in:
            require_value(obj_in["project_id"], "project_id")
        if "profile_code" in obj_in:
            require_value(obj_in["profile_code"], "profile_code")

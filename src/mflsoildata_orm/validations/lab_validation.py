from sqlalchemy.orm import Session

from ..models import Lab
from ..schemas.lab_schema import LabCreate
from .base import require_value, validate_unique


class LabValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: LabCreate) -> None:
        require_value(obj_in.lab_code, "lab_code")
        require_value(obj_in.name, "name")
        validate_unique(db, Lab, "lab_code", obj_in.lab_code)

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "lab_code" in obj_in:
            require_value(obj_in["lab_code"], "lab_code")
            validate_unique(db, Lab, "lab_code", obj_in["lab_code"], exclude_id=obj_id)
        if "name" in obj_in:
            require_value(obj_in["name"], "name")

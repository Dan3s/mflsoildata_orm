from sqlalchemy.orm import Session

from ..models import Variable
from ..schemas.variable_schema import VariableCreate
from .base import require_value, validate_unique


class VariableValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: VariableCreate) -> None:
        require_value(obj_in.variable_code, "variable_code")
        require_value(obj_in.name, "name")
        require_value(obj_in.domain, "domain")
        require_value(obj_in.value_type, "value_type")
        validate_unique(db, Variable, "variable_code", obj_in.variable_code)

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "variable_code" in obj_in:
            require_value(obj_in["variable_code"], "variable_code")
            validate_unique(
                db,
                Variable,
                "variable_code",
                obj_in["variable_code"],
                exclude_id=obj_id,
            )
        if "name" in obj_in:
            require_value(obj_in["name"], "name")
        if "domain" in obj_in:
            require_value(obj_in["domain"], "domain")
        if "value_type" in obj_in:
            require_value(obj_in["value_type"], "value_type")

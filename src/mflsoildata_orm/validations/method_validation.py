from sqlalchemy.orm import Session

from ..models import Method
from ..schemas.method_schema import MethodCreate
from .base import require_value, validate_unique


class MethodValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: MethodCreate) -> None:
        require_value(obj_in.method_code, "method_code")
        require_value(obj_in.name, "name")
        validate_unique(db, Method, "method_code", obj_in.method_code)

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "method_code" in obj_in:
            require_value(obj_in["method_code"], "method_code")
            validate_unique(
                db, Method, "method_code", obj_in["method_code"], exclude_id=obj_id
            )
        if "name" in obj_in:
            require_value(obj_in["name"], "name")

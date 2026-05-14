from sqlalchemy.orm import Session

from ..models import Unit
from ..schemas.unit_schema import UnitCreate
from .base import require_value, validate_unique


class UnitValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: UnitCreate) -> None:
        require_value(obj_in.unit_code, "unit_code")
        require_value(obj_in.symbol, "symbol")
        validate_unique(db, Unit, "unit_code", obj_in.unit_code)

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "unit_code" in obj_in:
            require_value(obj_in["unit_code"], "unit_code")
            validate_unique(db, Unit, "unit_code", obj_in["unit_code"], exclude_id=obj_id)
        if "symbol" in obj_in:
            require_value(obj_in["symbol"], "symbol")

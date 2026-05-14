from sqlalchemy.orm import Session

from ..schemas.measurement_schema import MeasurementCreate
from .base import require_value


class MeasurementValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: MeasurementCreate) -> None:
        require_value(obj_in.sample_id, "sample_id")
        require_value(obj_in.variable_id, "variable_id")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "sample_id" in obj_in:
            require_value(obj_in["sample_id"], "sample_id")
        if "variable_id" in obj_in:
            require_value(obj_in["variable_id"], "variable_id")

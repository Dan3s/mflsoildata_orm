from sqlalchemy.orm import Session

from ..models import Measurement
from ..schemas.measurement_schema import MeasurementCreate, MeasurementRead, MeasurementUpdate
from ..validations.measurement_validation import MeasurementValidator
from .base_service import BaseService


class MeasurementService(
    BaseService[Measurement, MeasurementCreate, MeasurementRead, MeasurementUpdate]
):
    def __init__(self) -> None:
        super().__init__(Measurement, MeasurementCreate, MeasurementRead, MeasurementUpdate)

    def _validate_create(self, obj_in: MeasurementCreate, db: Session) -> None:
        MeasurementValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        MeasurementValidator.update_validate(db, obj_in, obj_id)

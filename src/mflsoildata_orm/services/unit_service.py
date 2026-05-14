from sqlalchemy.orm import Session

from ..models import Unit
from ..schemas.unit_schema import UnitCreate, UnitRead, UnitUpdate
from ..validations.unit_validation import UnitValidator
from .base_service import BaseService


class UnitService(BaseService[Unit, UnitCreate, UnitRead, UnitUpdate]):
    def __init__(self) -> None:
        super().__init__(Unit, UnitCreate, UnitRead, UnitUpdate)

    def _validate_create(self, obj_in: UnitCreate, db: Session) -> None:
        UnitValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        UnitValidator.update_validate(db, obj_in, obj_id)

from sqlalchemy.orm import Session

from ..models import Lab
from ..schemas.lab_schema import LabCreate, LabRead, LabUpdate
from ..validations.lab_validation import LabValidator
from .base_service import BaseService


class LabService(BaseService[Lab, LabCreate, LabRead, LabUpdate]):
    def __init__(self) -> None:
        super().__init__(Lab, LabCreate, LabRead, LabUpdate)

    def _validate_create(self, obj_in: LabCreate, db: Session) -> None:
        LabValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        LabValidator.update_validate(db, obj_in, obj_id)

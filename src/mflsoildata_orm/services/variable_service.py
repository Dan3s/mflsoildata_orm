from sqlalchemy.orm import Session

from ..models import Variable
from ..schemas.variable_schema import VariableCreate, VariableRead, VariableUpdate
from ..validations.variable_validation import VariableValidator
from .base_service import BaseService


class VariableService(BaseService[Variable, VariableCreate, VariableRead, VariableUpdate]):
    def __init__(self) -> None:
        super().__init__(Variable, VariableCreate, VariableRead, VariableUpdate)

    def _validate_create(self, obj_in: VariableCreate, db: Session) -> None:
        VariableValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        VariableValidator.update_validate(db, obj_in, obj_id)

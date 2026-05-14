from sqlalchemy.orm import Session

from ..models import Method
from ..schemas.method_schema import MethodCreate, MethodRead, MethodUpdate
from ..validations.method_validation import MethodValidator
from .base_service import BaseService


class MethodService(BaseService[Method, MethodCreate, MethodRead, MethodUpdate]):
    def __init__(self) -> None:
        super().__init__(Method, MethodCreate, MethodRead, MethodUpdate)

    def _validate_create(self, obj_in: MethodCreate, db: Session) -> None:
        MethodValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        MethodValidator.update_validate(db, obj_in, obj_id)

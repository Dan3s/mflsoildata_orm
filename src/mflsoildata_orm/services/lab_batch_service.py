from sqlalchemy.orm import Session

from ..models import LabBatch
from ..schemas.lab_batch_schema import LabBatchCreate, LabBatchRead, LabBatchUpdate
from ..validations.lab_batch_validation import LabBatchValidator
from .base_service import BaseService


class LabBatchService(BaseService[LabBatch, LabBatchCreate, LabBatchRead, LabBatchUpdate]):
    def __init__(self) -> None:
        super().__init__(LabBatch, LabBatchCreate, LabBatchRead, LabBatchUpdate)

    def _validate_create(self, obj_in: LabBatchCreate, db: Session) -> None:
        LabBatchValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        LabBatchValidator.update_validate(db, obj_in, obj_id)

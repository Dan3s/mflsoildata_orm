from sqlalchemy.orm import Session

from ..schemas.lab_batch_schema import LabBatchCreate
from .base import require_value


class LabBatchValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: LabBatchCreate) -> None:
        require_value(obj_in.sample_id, "sample_id")
        require_value(obj_in.lab_id, "lab_id")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "sample_id" in obj_in:
            require_value(obj_in["sample_id"], "sample_id")
        if "lab_id" in obj_in:
            require_value(obj_in["lab_id"], "lab_id")

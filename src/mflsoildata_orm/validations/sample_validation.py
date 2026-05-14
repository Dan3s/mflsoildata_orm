from sqlalchemy.orm import Session

from ..schemas.sample_schema import SampleCreate
from .base import require_value


class SampleValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SampleCreate) -> None:
        require_value(obj_in.sample_type_id, "sample_type_id")
        require_value(obj_in.sample_code, "sample_code")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "sample_type_id" in obj_in:
            require_value(obj_in["sample_type_id"], "sample_type_id")
        if "sample_code" in obj_in:
            require_value(obj_in["sample_code"], "sample_code")

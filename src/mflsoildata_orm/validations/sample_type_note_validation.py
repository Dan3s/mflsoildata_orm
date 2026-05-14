from sqlalchemy.orm import Session

from ..schemas.sample_type_note_schema import SampleTypeNoteCreate
from .base import require_value


class SampleTypeNoteValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SampleTypeNoteCreate) -> None:
        require_value(obj_in.sample_id, "sample_id")
        require_value(obj_in.notes, "notes")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "sample_id" in obj_in:
            require_value(obj_in["sample_id"], "sample_id")
        if "notes" in obj_in:
            require_value(obj_in["notes"], "notes")

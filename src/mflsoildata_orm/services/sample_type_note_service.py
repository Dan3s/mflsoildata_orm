from sqlalchemy.orm import Session

from ..models import SampleTypeNote
from ..schemas.sample_type_note_schema import (
    SampleTypeNoteCreate,
    SampleTypeNoteRead,
    SampleTypeNoteUpdate,
)
from ..validations.sample_type_note_validation import SampleTypeNoteValidator
from .base_service import BaseService


class SampleTypeNoteService(
    BaseService[SampleTypeNote, SampleTypeNoteCreate, SampleTypeNoteRead, SampleTypeNoteUpdate]
):
    def __init__(self) -> None:
        super().__init__(
            SampleTypeNote, SampleTypeNoteCreate, SampleTypeNoteRead, SampleTypeNoteUpdate
        )

    def _validate_create(self, obj_in: SampleTypeNoteCreate, db: Session) -> None:
        SampleTypeNoteValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SampleTypeNoteValidator.update_validate(db, obj_in, obj_id)

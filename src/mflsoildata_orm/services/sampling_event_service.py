from sqlalchemy.orm import Session

from ..models import SamplingEvent
from ..schemas.sampling_event_schema import (
    SamplingEventCreate,
    SamplingEventRead,
    SamplingEventUpdate,
)
from ..validations.sampling_event_validation import SamplingEventValidator
from .base_service import BaseService


class SamplingEventService(
    BaseService[SamplingEvent, SamplingEventCreate, SamplingEventRead, SamplingEventUpdate]
):
    def __init__(self) -> None:
        super().__init__(
            SamplingEvent, SamplingEventCreate, SamplingEventRead, SamplingEventUpdate
        )

    def _validate_create(self, obj_in: SamplingEventCreate, db: Session) -> None:
        SamplingEventValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SamplingEventValidator.update_validate(db, obj_in, obj_id)

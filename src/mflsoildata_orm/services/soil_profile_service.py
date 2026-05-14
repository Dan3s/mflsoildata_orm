from sqlalchemy.orm import Session

from ..models import SoilProfile
from ..schemas.soil_profile_schema import SoilProfileCreate, SoilProfileRead, SoilProfileUpdate
from ..validations.soil_profile_validation import SoilProfileValidator
from .base_service import BaseService


class SoilProfileService(
    BaseService[SoilProfile, SoilProfileCreate, SoilProfileRead, SoilProfileUpdate]
):
    def __init__(self) -> None:
        super().__init__(SoilProfile, SoilProfileCreate, SoilProfileRead, SoilProfileUpdate)

    def _validate_create(self, obj_in: SoilProfileCreate, db: Session) -> None:
        SoilProfileValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SoilProfileValidator.update_validate(db, obj_in, obj_id)

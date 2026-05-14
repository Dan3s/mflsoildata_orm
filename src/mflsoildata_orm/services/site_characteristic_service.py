from sqlalchemy.orm import Session

from ..models import SiteCharacteristic
from ..schemas.site_characteristic_schema import (
    SiteCharacteristicCreate,
    SiteCharacteristicRead,
    SiteCharacteristicUpdate,
)
from ..validations.site_characteristic_validation import SiteCharacteristicValidator
from .base_service import BaseService


class SiteCharacteristicService(
    BaseService[SiteCharacteristic, SiteCharacteristicCreate, SiteCharacteristicRead, SiteCharacteristicUpdate]
):
    def __init__(self) -> None:
        super().__init__(
            SiteCharacteristic,
            SiteCharacteristicCreate,
            SiteCharacteristicRead,
            SiteCharacteristicUpdate,
        )

    def _validate_create(self, obj_in: SiteCharacteristicCreate, db: Session) -> None:
        SiteCharacteristicValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SiteCharacteristicValidator.update_validate(db, obj_in, obj_id)

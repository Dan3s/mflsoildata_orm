from sqlalchemy.orm import Session

from ..schemas.site_characteristic_schema import SiteCharacteristicCreate
from .base import require_value


class SiteCharacteristicValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SiteCharacteristicCreate) -> None:
        require_value(obj_in.site_id, "site_id")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "site_id" in obj_in:
            require_value(obj_in["site_id"], "site_id")

from sqlalchemy.orm import Session

from ..models import Site
from ..schemas.site_schema import SiteCreate, SiteRead, SiteUpdate
from ..validations.site_validation import SiteValidator
from .base_service import BaseService


class SiteService(BaseService[Site, SiteCreate, SiteRead, SiteUpdate]):
    def __init__(self) -> None:
        super().__init__(Site, SiteCreate, SiteRead, SiteUpdate)

    def _validate_create(self, obj_in: SiteCreate, db: Session) -> None:
        SiteValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        SiteValidator.update_validate(db, obj_in, obj_id)

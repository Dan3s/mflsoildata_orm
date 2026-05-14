from sqlalchemy.orm import Session

from ..schemas.site_schema import SiteCreate
from .base import require_value


class SiteValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SiteCreate) -> None:
        require_value(obj_in.project_id, "project_id")
        require_value(obj_in.site_code, "site_code")
        require_value(obj_in.geom, "geom")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "project_id" in obj_in:
            require_value(obj_in["project_id"], "project_id")
        if "site_code" in obj_in:
            require_value(obj_in["site_code"], "site_code")
        if "geom" in obj_in:
            require_value(obj_in["geom"], "geom")

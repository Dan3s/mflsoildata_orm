from sqlalchemy.orm import Session

from ..schemas.sampling_event_schema import SamplingEventCreate
from .base import require_value


class SamplingEventValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: SamplingEventCreate) -> None:
        require_value(obj_in.project_id, "project_id")
        require_value(obj_in.site_id, "site_id")

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "project_id" in obj_in:
            require_value(obj_in["project_id"], "project_id")
        if "site_id" in obj_in:
            require_value(obj_in["site_id"], "site_id")

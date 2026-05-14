from sqlalchemy.orm import Session

from ..models import Project
from ..schemas.project_schema import ProjectCreate
from .base import require_value, validate_unique


class ProjectValidator:
    @staticmethod
    def create_validate(db: Session, obj_in: ProjectCreate) -> None:
        require_value(obj_in.code, "code")
        require_value(obj_in.name, "name")
        validate_unique(db, Project, "code", obj_in.code)

    @staticmethod
    def update_validate(db: Session, obj_in: dict, obj_id: int) -> None:
        if "code" in obj_in:
            require_value(obj_in["code"], "code")
            validate_unique(db, Project, "code", obj_in["code"], exclude_id=obj_id)
        if "name" in obj_in:
            require_value(obj_in["name"], "name")

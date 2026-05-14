from sqlalchemy.orm import Session

from ..models import Project
from ..schemas.project_schema import ProjectCreate, ProjectRead, ProjectUpdate
from ..validations.project_validation import ProjectValidator
from .base_service import BaseService


class ProjectService(BaseService[Project, ProjectCreate, ProjectRead, ProjectUpdate]):
    def __init__(self) -> None:
        super().__init__(Project, ProjectCreate, ProjectRead, ProjectUpdate)

    def _validate_create(self, obj_in: ProjectCreate, db: Session) -> None:
        ProjectValidator.create_validate(db, obj_in)

    def _validate_update(self, obj_in: dict, db: Session, obj_id: int) -> None:
        ProjectValidator.update_validate(db, obj_in, obj_id)

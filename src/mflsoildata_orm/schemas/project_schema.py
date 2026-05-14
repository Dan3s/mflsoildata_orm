from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    code: str
    name: str
    country: Optional[str] = None
    donor: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    code: Optional[str] = None
    name: Optional[str] = None
    country: Optional[str] = None
    donor: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class ProjectRead(ProjectBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

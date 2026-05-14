from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SoilProfileBase(BaseModel):
    project_id: int
    site_id: Optional[int] = None
    event_id: Optional[int] = None
    profile_code: str
    notes: Optional[Dict[str, Any]] = None


class SoilProfileCreate(SoilProfileBase):
    pass


class SoilProfileUpdate(BaseModel):
    project_id: Optional[int] = None
    site_id: Optional[int] = None
    event_id: Optional[int] = None
    profile_code: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class SoilProfileRead(SoilProfileBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

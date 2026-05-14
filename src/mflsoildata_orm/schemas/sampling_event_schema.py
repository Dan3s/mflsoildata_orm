from datetime import date, datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SamplingEventBase(BaseModel):
    project_id: int
    site_id: int
    event_type: Optional[str] = None
    activity: Optional[str] = None
    event_date: Optional[date] = None
    organization: Optional[str] = None
    responsible: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class SamplingEventCreate(SamplingEventBase):
    pass


class SamplingEventUpdate(BaseModel):
    project_id: Optional[int] = None
    site_id: Optional[int] = None
    event_type: Optional[str] = None
    activity: Optional[str] = None
    event_date: Optional[date] = None
    organization: Optional[str] = None
    responsible: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class SamplingEventRead(SamplingEventBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SampleBase(BaseModel):
    event_id: Optional[int] = None
    site_id: Optional[int] = None
    sample_type_id: int
    sample_code: str
    parent_sample_id: Optional[int] = None
    notes: Optional[Dict[str, Any]] = None


class SampleCreate(SampleBase):
    pass


class SampleUpdate(BaseModel):
    event_id: Optional[int] = None
    site_id: Optional[int] = None
    sample_type_id: Optional[int] = None
    sample_code: Optional[str] = None
    parent_sample_id: Optional[int] = None
    notes: Optional[Dict[str, Any]] = None


class SampleRead(SampleBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

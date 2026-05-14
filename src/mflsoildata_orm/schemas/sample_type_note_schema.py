from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SampleTypeNoteBase(BaseModel):
    sample_id: int
    notes: Dict[str, Any]


class SampleTypeNoteCreate(SampleTypeNoteBase):
    pass


class SampleTypeNoteUpdate(BaseModel):
    sample_id: Optional[int] = None
    notes: Optional[Dict[str, Any]] = None


class SampleTypeNoteRead(SampleTypeNoteBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

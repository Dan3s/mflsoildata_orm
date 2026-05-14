from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SampleTypeBase(BaseModel):
    sample_type_code: str
    name: str
    notes: Optional[Dict[str, Any]] = None


class SampleTypeCreate(SampleTypeBase):
    pass


class SampleTypeUpdate(BaseModel):
    sample_type_code: Optional[str] = None
    name: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class SampleTypeRead(SampleTypeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

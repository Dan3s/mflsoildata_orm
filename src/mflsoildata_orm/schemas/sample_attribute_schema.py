from datetime import datetime
from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, ConfigDict


class SampleAttributeBase(BaseModel):
    sample_attribute_code: str
    name: str
    description: Optional[str] = None
    value_type: Literal["numeric", "text", "boolean", "date"]
    default_unit_id: Optional[int] = None
    category: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class SampleAttributeCreate(SampleAttributeBase):
    pass


class SampleAttributeUpdate(BaseModel):
    sample_attribute_code: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    value_type: Optional[Literal["numeric", "text", "boolean", "date"]] = None
    default_unit_id: Optional[int] = None
    category: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class SampleAttributeRead(SampleAttributeBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

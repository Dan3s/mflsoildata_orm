from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class LabBase(BaseModel):
    lab_code: str
    name: str
    scope: Optional[str] = None
    organization: Optional[str] = None
    country: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class LabCreate(LabBase):
    pass


class LabUpdate(BaseModel):
    lab_code: Optional[str] = None
    name: Optional[str] = None
    scope: Optional[str] = None
    organization: Optional[str] = None
    country: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class LabRead(LabBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

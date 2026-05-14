from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class MethodBase(BaseModel):
    method_code: str
    name: str
    extractant: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class MethodCreate(MethodBase):
    pass


class MethodUpdate(BaseModel):
    method_code: Optional[str] = None
    name: Optional[str] = None
    extractant: Optional[str] = None
    description: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class MethodRead(MethodBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

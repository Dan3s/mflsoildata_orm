from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SiteBase(BaseModel):
    project_id: int
    site_code: str
    country: Optional[str] = None
    admin_1: Optional[str] = None
    admin_2: Optional[str] = None
    admin_3: Optional[str] = None
    altitude_m: Optional[float] = None
    geom: Any
    location_notes: Optional[Dict[str, Any]] = None
    notes: Optional[Dict[str, Any]] = None


class SiteCreate(SiteBase):
    pass


class SiteUpdate(BaseModel):
    project_id: Optional[int] = None
    site_code: Optional[str] = None
    country: Optional[str] = None
    admin_1: Optional[str] = None
    admin_2: Optional[str] = None
    admin_3: Optional[str] = None
    altitude_m: Optional[float] = None
    geom: Optional[Any] = None
    location_notes: Optional[Dict[str, Any]] = None
    notes: Optional[Dict[str, Any]] = None


class SiteRead(SiteBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SiteCharacteristicBase(BaseModel):
    site_id: int
    profile_info: Optional[Dict[str, Any]] = None
    site_info: Optional[Dict[str, Any]] = None
    sampling_info: Optional[Dict[str, Any]] = None
    notes: Optional[Dict[str, Any]] = None


class SiteCharacteristicCreate(SiteCharacteristicBase):
    pass


class SiteCharacteristicUpdate(BaseModel):
    site_id: Optional[int] = None
    profile_info: Optional[Dict[str, Any]] = None
    site_info: Optional[Dict[str, Any]] = None
    sampling_info: Optional[Dict[str, Any]] = None
    notes: Optional[Dict[str, Any]] = None


class SiteCharacteristicRead(SiteCharacteristicBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

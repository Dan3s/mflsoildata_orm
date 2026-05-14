from datetime import date, datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class SiteAttributeValueBase(BaseModel):
    site_id: int
    site_attribute_id: int
    unit_id: Optional[int] = None
    value_numeric: Optional[float] = None
    value_text: Optional[str] = None
    value_boolean: Optional[bool] = None
    value_date: Optional[date] = None
    effective_date: Optional[date] = None
    source_name: Optional[str] = None
    source_ref: Optional[str] = None
    confidence: Optional[float] = None
    notes: Optional[Dict[str, Any]] = None


class SiteAttributeValueCreate(SiteAttributeValueBase):
    pass


class SiteAttributeValueUpdate(BaseModel):
    site_id: Optional[int] = None
    site_attribute_id: Optional[int] = None
    unit_id: Optional[int] = None
    value_numeric: Optional[float] = None
    value_text: Optional[str] = None
    value_boolean: Optional[bool] = None
    value_date: Optional[date] = None
    effective_date: Optional[date] = None
    source_name: Optional[str] = None
    source_ref: Optional[str] = None
    confidence: Optional[float] = None
    notes: Optional[Dict[str, Any]] = None


class SiteAttributeValueRead(SiteAttributeValueBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class LabBatchBase(BaseModel):
    sample_id: int
    lab_id: int
    method_id: Optional[int] = None
    lab_batch_code: Optional[str] = None
    lab_reference: Optional[str] = None
    lab_sample_id: Optional[str] = None
    lab_shipment_id: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class LabBatchCreate(LabBatchBase):
    pass


class LabBatchUpdate(BaseModel):
    sample_id: Optional[int] = None
    lab_id: Optional[int] = None
    method_id: Optional[int] = None
    lab_batch_code: Optional[str] = None
    lab_reference: Optional[str] = None
    lab_sample_id: Optional[str] = None
    lab_shipment_id: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class LabBatchRead(LabBatchBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

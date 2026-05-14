from datetime import date, datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class MeasurementBase(BaseModel):
    measurement_code: Optional[str] = None
    sample_id: int
    variable_id: int
    lab_batch_id: Optional[int] = None
    unit_id: Optional[int] = None
    value_numeric: Optional[float] = None
    value_text: Optional[str] = None
    value_boolean: Optional[bool] = None
    value_date: Optional[date] = None
    qualifier_result: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class MeasurementCreate(MeasurementBase):
    pass


class MeasurementUpdate(BaseModel):
    measurement_code: Optional[str] = None
    sample_id: Optional[int] = None
    variable_id: Optional[int] = None
    lab_batch_id: Optional[int] = None
    unit_id: Optional[int] = None
    value_numeric: Optional[float] = None
    value_text: Optional[str] = None
    value_boolean: Optional[bool] = None
    value_date: Optional[date] = None
    qualifier_result: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class MeasurementRead(MeasurementBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)

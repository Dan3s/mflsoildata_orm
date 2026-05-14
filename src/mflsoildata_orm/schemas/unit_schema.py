from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict


class UnitBase(BaseModel):
    unit_code: str
    symbol: str
    dimension: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class UnitCreate(UnitBase):
    pass


class UnitUpdate(BaseModel):
    unit_code: Optional[str] = None
    symbol: Optional[str] = None
    dimension: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class UnitRead(UnitBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

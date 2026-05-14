from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, ConfigDict


class VariableBase(BaseModel):
    variable_code: str
    name: str
    domain: str
    matrix: Optional[str] = None
    value_type: Literal["numeric", "text", "boolean", "date"]
    default_unit_id: Optional[int] = None
    description: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class VariableCreate(VariableBase):
    pass


class VariableUpdate(BaseModel):
    variable_code: Optional[str] = None
    name: Optional[str] = None
    domain: Optional[str] = None
    matrix: Optional[str] = None
    value_type: Optional[Literal["numeric", "text", "boolean", "date"]] = None
    default_unit_id: Optional[int] = None
    description: Optional[str] = None
    notes: Optional[Dict[str, Any]] = None


class VariableRead(VariableBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

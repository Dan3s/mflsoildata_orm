from typing import Any, Optional

from sqlalchemy.orm import Session


def require_value(value: Any, field_name: str) -> None:
    if value is None:
        raise ValueError(f"{field_name} is required.")
    if isinstance(value, str) and not value.strip():
        raise ValueError(f"{field_name} is required.")


def validate_unique(
    db: Session,
    model,
    field_name: str,
    value: Any,
    exclude_id: Optional[int] = None,
) -> None:
    if value is None:
        return
    field = getattr(model, field_name)
    query = db.query(model).filter(field == value)
    if exclude_id is not None:
        query = query.filter(model.id != exclude_id)
    if query.first() is not None:
        raise ValueError(f"{model.__name__} with {field_name} '{value}' already exists.")

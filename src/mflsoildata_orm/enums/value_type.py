from enum import Enum


class ValueType(str, Enum):
    NUMERIC = "numeric"
    TEXT = "text"
    BOOLEAN = "boolean"
    DATE = "date"

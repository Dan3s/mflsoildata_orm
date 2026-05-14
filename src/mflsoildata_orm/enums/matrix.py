from enum import Enum


class Matrix(str, Enum):
    SOIL = "SOIL"
    LEAF = "LEAF"
    GRAIN = "GRAIN"
    SOIL_PROFILE = "SOIL_PROFILE"
    SOIL_HORIZON = "SOIL_HORIZON"

from sqlalchemy import BigInteger, Column, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from ..database.base import Base


class Unit(Base):
    __tablename__ = "units"

    id = Column(BigInteger, primary_key=True)
    unit_code = Column(String, nullable=False, unique=True)
    symbol = Column(String, nullable=False)
    dimension = Column(String)
    notes = Column(JSONB)

    variables = relationship("Variable", back_populates="default_unit")
    sample_attributes = relationship("SampleAttribute", back_populates="default_unit")
    soil_profile_attributes = relationship(
        "SoilProfileAttribute", back_populates="default_unit"
    )
    site_attributes = relationship("SiteAttribute", back_populates="default_unit")
    sample_attribute_values = relationship(
        "SampleAttributeValue", back_populates="unit"
    )
    soil_profile_attribute_values = relationship(
        "SoilProfileAttributeValue", back_populates="unit"
    )
    site_attribute_values = relationship("SiteAttributeValue", back_populates="unit")
    measurements = relationship("Measurement", back_populates="unit")

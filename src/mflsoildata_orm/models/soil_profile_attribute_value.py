from sqlalchemy import (
    BigInteger,
    Boolean,
    CheckConstraint,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class SoilProfileAttributeValue(Base):
    __tablename__ = "soil_profile_attribute_values"
    __table_args__ = (
        UniqueConstraint(
            "soil_profile_id",
            "soil_profile_attribute_id",
            "effective_date",
            name="uq_soil_profile_attr_values_profile_attr_date",
        ),
        CheckConstraint(
            "(CASE WHEN value_numeric IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_text IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_boolean IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_date IS NOT NULL THEN 1 ELSE 0 END) <= 1",
            name="ck_soil_profile_attr_values_one_value_only",
        ),
    )

    id = Column(BigInteger, primary_key=True)
    soil_profile_id = Column(
        BigInteger, ForeignKey("soil_profiles.id", ondelete="CASCADE"), nullable=False
    )
    soil_profile_attribute_id = Column(
        BigInteger,
        ForeignKey("soil_profile_attributes.id", ondelete="CASCADE"),
        nullable=False,
    )
    unit_id = Column(BigInteger, ForeignKey("units.id", ondelete="SET NULL"))

    value_numeric = Column(Numeric)
    value_text = Column(Text)
    value_boolean = Column(Boolean)
    value_date = Column(Date)

    effective_date = Column(Date)
    source_name = Column(String)
    source_ref = Column(String)
    confidence = Column(Numeric)

    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    soil_profile = relationship("SoilProfile", back_populates="attributes")
    soil_profile_attribute = relationship(
        "SoilProfileAttribute", back_populates="values"
    )
    unit = relationship("Unit", back_populates="soil_profile_attribute_values")

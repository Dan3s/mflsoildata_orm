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


class SampleAttributeValue(Base):
    __tablename__ = "sample_attribute_values"
    __table_args__ = (
        UniqueConstraint(
            "sample_id",
            "sample_attribute_id",
            "effective_date",
            name="uq_sample_attr_values_sample_attr_date",
        ),
        CheckConstraint(
            "(CASE WHEN value_numeric IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_text IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_boolean IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_date IS NOT NULL THEN 1 ELSE 0 END) <= 1",
            name="ck_sample_attr_values_one_value_only",
        ),
    )

    id = Column(BigInteger, primary_key=True)
    sample_id = Column(
        BigInteger, ForeignKey("samples.id", ondelete="CASCADE"), nullable=False
    )
    sample_attribute_id = Column(
        BigInteger, ForeignKey("sample_attributes.id", ondelete="CASCADE"), nullable=False
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

    sample = relationship("Sample", back_populates="attributes")
    sample_attribute = relationship("SampleAttribute", back_populates="values")
    unit = relationship("Unit", back_populates="sample_attribute_values")

from sqlalchemy import (
    BigInteger,
    CheckConstraint,
    Column,
    DateTime,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class SampleAttribute(Base):
    __tablename__ = "sample_attributes"
    __table_args__ = (
        CheckConstraint(
            "value_type IN ('numeric','text','boolean','date')",
            name="ck_sample_attributes_value_type",
        ),
    )

    id = Column(BigInteger, primary_key=True)
    sample_attribute_code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    value_type = Column(String, nullable=False)
    default_unit_id = Column(BigInteger, ForeignKey("units.id", ondelete="SET NULL"))
    category = Column(String)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    default_unit = relationship("Unit", back_populates="sample_attributes")
    values = relationship("SampleAttributeValue", back_populates="sample_attribute")

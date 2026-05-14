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


class Measurement(Base):
    __tablename__ = "measurements"
    __table_args__ = (
        UniqueConstraint(
            "sample_id",
            "variable_id",
            "lab_batch_id",
            name="uq_measurements_sample_variable_batch",
        ),
        CheckConstraint(
            "(CASE WHEN value_numeric IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_text IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_boolean IS NOT NULL THEN 1 ELSE 0 END + "
            "CASE WHEN value_date IS NOT NULL THEN 1 ELSE 0 END) <= 1",
            name="ck_measurements_one_value_only",
        ),
    )

    id = Column(BigInteger, primary_key=True)
    measurement_code = Column(String, unique=True)
    sample_id = Column(
        BigInteger, ForeignKey("samples.id", ondelete="CASCADE"), nullable=False
    )
    variable_id = Column(
        BigInteger, ForeignKey("variables.id", ondelete="RESTRICT"), nullable=False
    )
    lab_batch_id = Column(BigInteger, ForeignKey("lab_batches.id", ondelete="SET NULL"))
    unit_id = Column(BigInteger, ForeignKey("units.id", ondelete="SET NULL"))

    value_numeric = Column(Numeric)
    value_text = Column(Text)
    value_boolean = Column(Boolean)
    value_date = Column(Date)

    qualifier_result = Column(String)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    sample = relationship("Sample", back_populates="measurements")
    variable = relationship("Variable", back_populates="measurements")
    lab_batch = relationship("LabBatch", back_populates="measurements")
    unit = relationship("Unit", back_populates="measurements")

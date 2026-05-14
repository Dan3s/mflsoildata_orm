from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class LabBatch(Base):
    __tablename__ = "lab_batches"
    __table_args__ = (
        UniqueConstraint(
            "sample_id", "lab_id", "lab_batch_code", name="uq_lab_batches_sample_lab_batch"
        ),
    )

    id = Column(BigInteger, primary_key=True)
    sample_id = Column(
        BigInteger, ForeignKey("samples.id", ondelete="CASCADE"), nullable=False
    )
    lab_id = Column(BigInteger, ForeignKey("labs.id", ondelete="RESTRICT"), nullable=False)
    method_id = Column(BigInteger, ForeignKey("methods.id", ondelete="SET NULL"))
    lab_batch_code = Column(String)
    lab_reference = Column(String)
    lab_sample_id = Column(String)
    lab_shipment_id = Column(String)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    sample = relationship("Sample", back_populates="lab_batches")
    lab = relationship("Lab", back_populates="lab_batches")
    method = relationship("Method", back_populates="lab_batches")
    measurements = relationship("Measurement", back_populates="lab_batch")

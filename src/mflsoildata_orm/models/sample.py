from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class Sample(Base):
    __tablename__ = "samples"
    __table_args__ = (
        UniqueConstraint("event_id", "sample_code", name="uq_samples_event_sample_code"),
    )

    id = Column(BigInteger, primary_key=True)
    event_id = Column(BigInteger, ForeignKey("sampling_events.id", ondelete="SET NULL"))
    site_id = Column(BigInteger, ForeignKey("sites.id", ondelete="SET NULL"))
    sample_type_id = Column(
        BigInteger, ForeignKey("sample_types.id", ondelete="RESTRICT"), nullable=False
    )
    sample_code = Column(String, nullable=False)
    parent_sample_id = Column(BigInteger, ForeignKey("samples.id", ondelete="SET NULL"))
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    event = relationship("SamplingEvent", back_populates="samples")
    site = relationship("Site", back_populates="samples")
    sample_type = relationship("SampleType", back_populates="samples")
    parent_sample = relationship(
        "Sample", remote_side=[id], back_populates="child_samples"
    )
    child_samples = relationship("Sample", back_populates="parent_sample")
    attributes = relationship("SampleAttributeValue", back_populates="sample")
    type_notes = relationship("SampleTypeNote", back_populates="sample")
    lab_batches = relationship("LabBatch", back_populates="sample")
    measurements = relationship("Measurement", back_populates="sample")

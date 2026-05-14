from sqlalchemy import BigInteger, Column, Date, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class SamplingEvent(Base):
    __tablename__ = "sampling_events"

    id = Column(BigInteger, primary_key=True)
    project_id = Column(
        BigInteger, ForeignKey("projects.id", ondelete="RESTRICT"), nullable=False
    )
    site_id = Column(
        BigInteger, ForeignKey("sites.id", ondelete="RESTRICT"), nullable=False
    )
    event_type = Column(String)
    activity = Column(String)
    event_date = Column(Date)
    organization = Column(String)
    responsible = Column(String)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    project = relationship("Project", back_populates="sampling_events")
    site = relationship("Site", back_populates="sampling_events")
    samples = relationship("Sample", back_populates="event")
    soil_profiles = relationship("SoilProfile", back_populates="event")

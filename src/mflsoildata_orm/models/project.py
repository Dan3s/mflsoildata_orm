from sqlalchemy import BigInteger, Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(BigInteger, primary_key=True)
    code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    country = Column(String)
    donor = Column(String)
    description = Column(Text)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    sites = relationship("Site", back_populates="project")
    sampling_events = relationship("SamplingEvent", back_populates="project")
    soil_profiles = relationship("SoilProfile", back_populates="project")

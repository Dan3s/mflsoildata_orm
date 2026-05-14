from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class SoilProfile(Base):
    __tablename__ = "soil_profiles"
    __table_args__ = (
        UniqueConstraint(
            "project_id", "profile_code", name="uq_soil_profiles_project_profile_code"
        ),
    )

    id = Column(BigInteger, primary_key=True)
    project_id = Column(
        BigInteger, ForeignKey("projects.id", ondelete="RESTRICT"), nullable=False
    )
    site_id = Column(BigInteger, ForeignKey("sites.id", ondelete="SET NULL"))
    event_id = Column(BigInteger, ForeignKey("sampling_events.id", ondelete="SET NULL"))
    profile_code = Column(String, nullable=False)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    project = relationship("Project", back_populates="soil_profiles")
    site = relationship("Site", back_populates="soil_profiles")
    event = relationship("SamplingEvent", back_populates="soil_profiles")
    attributes = relationship("SoilProfileAttributeValue", back_populates="soil_profile")

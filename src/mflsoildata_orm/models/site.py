from geoalchemy2 import Geometry
from sqlalchemy import (
    BigInteger,
    Column,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class Site(Base):
    __tablename__ = "sites"
    __table_args__ = (
        UniqueConstraint("project_id", "site_code", name="uq_sites_project_site_code"),
    )

    id = Column(BigInteger, primary_key=True)
    project_id = Column(
        BigInteger, ForeignKey("projects.id", ondelete="RESTRICT"), nullable=False
    )
    site_code = Column(String, nullable=False)
    country = Column(String)
    admin_1 = Column(String)
    admin_2 = Column(String)
    admin_3 = Column(String)
    altitude_m = Column(Numeric)
    geom = Column(Geometry(geometry_type="GEOMETRY", srid=4326), nullable=False)
    location_notes = Column(JSONB)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    project = relationship("Project", back_populates="sites")
    site_characteristics = relationship(
        "SiteCharacteristic", back_populates="site", uselist=False
    )
    sampling_events = relationship("SamplingEvent", back_populates="site")
    samples = relationship("Sample", back_populates="site")
    soil_profiles = relationship("SoilProfile", back_populates="site")
    site_attribute_values = relationship("SiteAttributeValue", back_populates="site")

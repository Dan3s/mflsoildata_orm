from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    String,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class ProjectMetadata(Base):
    """FAIR-aligned descriptive metadata for a project (1:1 with ``projects``).

    See docs/PROPUESTA_METADATOS.md. Fields are expected to evolve as they are
    confirmed with the team, so this is the initial agreed set.
    Enumerated values (``access_level``, ``qc_status``) are stored as text and
    validated in the application layer, matching the rest of the model.
    """

    __tablename__ = "project_metadata"

    id = Column(BigInteger, primary_key=True)
    project_id = Column(
        BigInteger,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    # Findable
    title = Column(String)
    abstract = Column(Text)
    keywords = Column(JSONB)
    persistent_id = Column(String)
    related_publications = Column(JSONB)
    version = Column(String)
    # Authors/creators, "Name (Affiliation)" per entry — distinct from
    # contact_name/contact_email below, which is the point of contact, not
    # necessarily who should be cited.
    authors = Column(JSONB)
    # Dataverse's compound grantNumber/contributor fields, combined into one
    # free-text field (e.g. "Grant 123 — Bill & Melinda Gates Foundation").
    funding_information = Column(Text)
    language = Column(String)
    # Other datasets this one relates to/continues (ours, Dataverse or CGSpace).
    related_datasets = Column(JSONB)
    # Discipline — Dataverse's controlled vocabulary is offered as suggestions
    # in the UI, but stored as free text: an imported dataset may carry a value
    # outside that list.
    subject = Column(String)
    # {west, east, north, south} as declared by the dataset's source (e.g. an
    # imported Dataverse dataset's geospatial block), not computed from our
    # own sites.
    geographic_bounding_box = Column(JSONB)

    # Coverage
    temporal_coverage_start = Column(Date)
    temporal_coverage_end = Column(Date)
    spatial_coverage = Column(Text)
    # Geometry the dataset describes: POINT | LINE | POLYGON.
    spatial_data_type = Column(String)
    # How the soil was sampled, as a list because a dataset can mix both:
    # FARM_COMPOSITE (one composite sample for a whole farm) | SINGLE_POINT (an
    # individual sample at one point).
    sampling_type = Column(JSONB)
    expected_matrices = Column(JSONB)
    expected_variables = Column(Text)
    sampling_design = Column(Text)

    # Accessible / privacy
    access_level = Column(String, nullable=False, server_default="PRIVATE")
    authorized_users = Column(JSONB)
    embargo_until = Column(Date)
    license = Column(String)
    access_conditions = Column(Text)

    # Reusable / provenance
    data_source = Column(String)
    # Research group (within the source organization) that produced the data.
    research_group = Column(String)
    provenance = Column(Text)
    methodology = Column(Text)
    citation = Column(Text)
    usage_notes = Column(Text)
    contact_name = Column(String)
    contact_email = Column(String)
    # Backup contact, in case the primary one doesn't answer.
    contact_name_2 = Column(String)
    contact_email_2 = Column(String)

    # Quality control
    quality_controlled = Column(Boolean, nullable=False, server_default=text("false"))
    qc_status = Column(String, nullable=False, server_default="NOT_REVIEWED")
    qc_date = Column(Date)
    qc_by = Column(String)
    qc_notes = Column(Text)

    # System
    data_last_updated = Column(Date)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # ``metadata`` collides with SQLAlchemy's ``Base.metadata``; use ``metadata_``.
    project = relationship("Project", back_populates="metadata_")

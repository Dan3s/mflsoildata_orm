from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from ..database.base import Base


class DatasetSubmission(Base):
    """Approval + traceability record for an uploaded dataset (one import event).

    A ``database_editor`` reviews PENDING submissions and approves/rejects them;
    the submitter is notified by email at each stage. Submitter/reviewer identity
    comes from Keycloak (stored denormalized, no FK to a users table).

    The uploaded rows are staged in ``submission_row`` and only replayed into the
    domain tables on approval, so pending data never reaches production tables.
    """

    __tablename__ = "dataset_submission"

    id = Column(BigInteger, primary_key=True)
    # NULL while PENDING: a brand-new project does not exist until approval.
    project_id = Column(BigInteger, ForeignKey("projects.id", ondelete="SET NULL"), nullable=True)
    project_code = Column(String)   # snapshot (survives project deletion)
    project_name = Column(String)
    project_codes = Column(JSONB)   # every distinct project code found in the file

    # --- staged upload (the "lote") ---
    filename = Column(String)
    column_ids = Column(JSONB)      # replayed into StoredUpload.column_ids on approval
    # Variables the uploader defined in the template's "New variables" sheet
    # (column ids ``newvar:<CODE>``). They do not exist in ``variables`` until a
    # database_editor approves, who may edit or merge them into an existing one.
    new_variables = Column(JSONB)
    total_rows = Column(Integer)
    summary = Column(JSONB)         # dry-run estimate shown before approval
    warning_count = Column(Integer)
    # FAIR metadata captured at upload time. A brand-new project does not exist
    # until approval, so its ficha has to wait here too and is applied to
    # ``project_metadata`` when the submission is approved.
    metadata_payload = Column(JSONB)

    submitted_by_sub = Column(String)
    submitted_by_email = Column(String)
    submitted_by_name = Column(String)
    organization = Column(String)
    country = Column(String)

    status = Column(String, nullable=False, server_default="PENDING")  # PENDING | APPROVED | REJECTED
    inserted = Column(JSONB)   # counts snapshot from the import

    submitted_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    reviewed_at = Column(DateTime(timezone=True))
    reviewed_by_email = Column(String)
    reviewed_by_name = Column(String)
    review_notes = Column(Text)

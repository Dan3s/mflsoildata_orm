from sqlalchemy import BigInteger, Column, ForeignKey, Index, Integer, String

from sqlalchemy.dialects.postgresql import JSONB

from ..database.base import Base


class SubmissionRow(Base):
    """One staged row of an uploaded file, held until the submission is reviewed.

    Staging area: an upload writes its parsed rows here and NOTHING into the real
    tables. On approval the ETL replays these rows into the domain model; on
    rejection they are dropped with the submission (FK CASCADE). This is what
    makes pending data invisible by construction instead of by query filters.

    ``data`` keeps the full parsed row (the same dict the ETL consumes). The
    natural-key columns are denormalized so the reviewer can filter/search a
    large file without scanning the JSONB.
    """

    __tablename__ = "submission_row"

    id = Column(BigInteger, primary_key=True)
    submission_id = Column(
        BigInteger,
        ForeignKey("dataset_submission.id", ondelete="CASCADE"),
        nullable=False,
    )

    row_number = Column(Integer)   # 1-based line in the source file
    project_code = Column(String)
    site_code = Column(String)
    sample_code = Column(String)

    data = Column(JSONB, nullable=False)


Index("ix_submission_row_submission", SubmissionRow.submission_id, SubmissionRow.row_number)
Index("ix_submission_row_sample", SubmissionRow.submission_id, SubmissionRow.sample_code)

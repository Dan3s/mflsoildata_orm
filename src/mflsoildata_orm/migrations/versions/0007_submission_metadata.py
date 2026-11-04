"""Stage the FAIR metadata alongside the uploaded rows.

A new project does not exist until its submission is approved, so the ficha the
uploader fills in cannot be written to ``project_metadata`` yet either.

Revision ID: 0007_submission_metadata
Revises: 0006_submission_staging
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0007_submission_metadata"
down_revision = "0006_submission_staging"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    existing = {
        r[0]
        for r in bind.execute(
            sa.text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name = 'dataset_submission'"
            )
        )
    }
    if "metadata_payload" not in existing:
        op.add_column(
            "dataset_submission",
            sa.Column("metadata_payload", postgresql.JSONB(), nullable=True),
        )


def downgrade() -> None:
    op.drop_column("dataset_submission", "metadata_payload")

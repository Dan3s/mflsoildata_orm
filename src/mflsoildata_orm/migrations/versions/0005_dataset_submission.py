"""Dataset approval / traceability submissions.

Revision ID: 0005_dataset_submission
Revises: 0004_download_log_org_country
Create Date: 2026-08-06
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0005_dataset_submission"
down_revision = "0004_download_log_org_country"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "dataset_submission" not in inspector.get_table_names():
        op.create_table(
            "dataset_submission",
            sa.Column("id", sa.BigInteger(), primary_key=True),
            sa.Column("project_id", sa.BigInteger(), nullable=True),
            sa.Column("project_code", sa.String(), nullable=True),
            sa.Column("project_name", sa.String(), nullable=True),
            sa.Column("submitted_by_sub", sa.String(), nullable=True),
            sa.Column("submitted_by_email", sa.String(), nullable=True),
            sa.Column("submitted_by_name", sa.String(), nullable=True),
            sa.Column("organization", sa.String(), nullable=True),
            sa.Column("country", sa.String(), nullable=True),
            sa.Column("status", sa.String(), server_default="PENDING", nullable=False),
            sa.Column("inserted", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("submitted_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
            sa.Column("reviewed_at", sa.DateTime(timezone=True), nullable=True),
            sa.Column("reviewed_by_email", sa.String(), nullable=True),
            sa.Column("reviewed_by_name", sa.String(), nullable=True),
            sa.Column("review_notes", sa.Text(), nullable=True),
            sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="SET NULL"),
        )
        op.create_index("ix_dataset_submission_status", "dataset_submission", ["status"])
        op.create_index("ix_dataset_submission_submitted_at", "dataset_submission", ["submitted_at"])


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "dataset_submission" in inspector.get_table_names():
        op.drop_index("ix_dataset_submission_submitted_at", table_name="dataset_submission")
        op.drop_index("ix_dataset_submission_status", table_name="dataset_submission")
        op.drop_table("dataset_submission")

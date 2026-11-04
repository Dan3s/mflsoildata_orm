"""FAIR project metadata (project_metadata).

Revision ID: 0003_project_metadata
Revises: 0002_download_log
Create Date: 2026-08-06
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0003_project_metadata"
down_revision = "0002_download_log"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    # Baseline uses create_all (model-driven), so on a fresh DB the table may
    # already exist; only create it when missing.
    if "project_metadata" not in inspector.get_table_names():
        op.create_table(
            "project_metadata",
            sa.Column("id", sa.BigInteger(), primary_key=True),
            sa.Column("project_id", sa.BigInteger(), nullable=False),
            # Findable
            sa.Column("title", sa.String(), nullable=True),
            sa.Column("abstract", sa.Text(), nullable=True),
            sa.Column("keywords", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("persistent_id", sa.String(), nullable=True),
            sa.Column("related_publications", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("version", sa.String(), nullable=True),
            # Coverage
            sa.Column("temporal_coverage_start", sa.Date(), nullable=True),
            sa.Column("temporal_coverage_end", sa.Date(), nullable=True),
            sa.Column("spatial_coverage", sa.Text(), nullable=True),
            sa.Column("expected_matrices", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("expected_variables", sa.Text(), nullable=True),
            sa.Column("sampling_design", sa.Text(), nullable=True),
            # Accessible / privacy
            sa.Column("access_level", sa.String(), server_default="PRIVATE", nullable=False),
            sa.Column("authorized_users", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("embargo_until", sa.Date(), nullable=True),
            sa.Column("license", sa.String(), nullable=True),
            sa.Column("access_conditions", sa.Text(), nullable=True),
            # Reusable / provenance
            sa.Column("data_source", sa.String(), nullable=True),
            sa.Column("provenance", sa.Text(), nullable=True),
            sa.Column("methodology", sa.Text(), nullable=True),
            sa.Column("citation", sa.Text(), nullable=True),
            sa.Column("usage_notes", sa.Text(), nullable=True),
            sa.Column("contact_name", sa.String(), nullable=True),
            sa.Column("contact_email", sa.String(), nullable=True),
            # Quality control
            sa.Column("quality_controlled", sa.Boolean(), server_default=sa.text("false"), nullable=False),
            sa.Column("qc_status", sa.String(), server_default="NOT_REVIEWED", nullable=False),
            sa.Column("qc_date", sa.Date(), nullable=True),
            sa.Column("qc_by", sa.String(), nullable=True),
            sa.Column("qc_notes", sa.Text(), nullable=True),
            # System
            sa.Column("data_last_updated", sa.Date(), nullable=True),
            sa.Column("notes", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
            sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
            sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
            sa.UniqueConstraint("project_id", name="uq_project_metadata_project_id"),
        )
        op.create_index("ix_project_metadata_access_level", "project_metadata", ["access_level"])


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "project_metadata" in inspector.get_table_names():
        op.drop_index("ix_project_metadata_access_level", table_name="project_metadata")
        op.drop_table("project_metadata")

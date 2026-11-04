"""Add organization/country to the download audit log (RF32).

Revision ID: 0004_download_log_org_country
Revises: 0003_project_metadata
Create Date: 2026-08-06
"""
from alembic import op
import sqlalchemy as sa

revision = "0004_download_log_org_country"
down_revision = "0003_project_metadata"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing = {c["name"] for c in inspector.get_columns("download_log")}
    if "organization" not in existing:
        op.add_column("download_log", sa.Column("organization", sa.String(), nullable=True))
    if "country" not in existing:
        op.add_column("download_log", sa.Column("country", sa.String(), nullable=True))


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    existing = {c["name"] for c in inspector.get_columns("download_log")}
    if "country" in existing:
        op.drop_column("download_log", "country")
    if "organization" in existing:
        op.drop_column("download_log", "organization")

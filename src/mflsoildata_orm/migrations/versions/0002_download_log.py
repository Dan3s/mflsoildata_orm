"""Download audit log (RF32).

Revision ID: 0002_download_log
Revises: 0001_baseline
Create Date: 2026-08-06
"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0002_download_log"
down_revision = "0001_baseline"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    # The baseline migration uses ``create_all`` (model-driven), so on a fresh DB
    # the table may already exist; only create it when missing.
    if "download_log" not in inspector.get_table_names():
        op.create_table(
            "download_log",
            sa.Column("id", sa.BigInteger(), primary_key=True),
            sa.Column("user_sub", sa.String(), nullable=True),
            sa.Column("user_email", sa.String(), nullable=True),
            sa.Column("username", sa.String(), nullable=True),
            sa.Column("format", sa.String(), nullable=False),
            sa.Column("record_count", sa.BigInteger(), nullable=True),
            sa.Column("filters", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
            sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        )
        op.create_index("ix_download_log_created_at", "download_log", ["created_at"])
        op.create_index("ix_download_log_user_sub", "download_log", ["user_sub"])


def downgrade() -> None:
    bind = op.get_bind()
    inspector = sa.inspect(bind)
    if "download_log" in inspector.get_table_names():
        op.drop_index("ix_download_log_user_sub", table_name="download_log")
        op.drop_index("ix_download_log_created_at", table_name="download_log")
        op.drop_table("download_log")

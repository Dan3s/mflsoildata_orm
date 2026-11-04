"""Stage uploaded rows until approval (submission_row + lote columns).

Uploads no longer write to the domain tables: the parsed rows land in
``submission_row`` and are replayed by the ETL when a database_editor approves.

Revision ID: 0006_submission_staging
Revises: 0005_dataset_submission
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0006_submission_staging"
down_revision = "0005_dataset_submission"
branch_labels = None
depends_on = None


_NEW_COLUMNS = [
    ("project_codes", postgresql.JSONB()),
    ("filename", sa.String()),
    ("column_ids", postgresql.JSONB()),
    ("total_rows", sa.Integer()),
    ("summary", postgresql.JSONB()),
    ("warning_count", sa.Integer()),
]


def _existing_columns(table: str):
    bind = op.get_bind()
    return {
        r[0]
        for r in bind.execute(
            sa.text("SELECT column_name FROM information_schema.columns WHERE table_name = :t"),
            {"t": table},
        )
    }


def upgrade() -> None:
    existing = _existing_columns("dataset_submission")
    for name, type_ in _NEW_COLUMNS:
        if name not in existing:
            op.add_column("dataset_submission", sa.Column(name, type_, nullable=True))

    bind = op.get_bind()
    has_table = bind.execute(
        sa.text("SELECT to_regclass('public.submission_row')")
    ).scalar()
    if has_table:
        return

    op.create_table(
        "submission_row",
        sa.Column("id", sa.BigInteger(), primary_key=True),
        sa.Column(
            "submission_id",
            sa.BigInteger(),
            sa.ForeignKey("dataset_submission.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("row_number", sa.Integer(), nullable=True),
        sa.Column("project_code", sa.String(), nullable=True),
        sa.Column("site_code", sa.String(), nullable=True),
        sa.Column("sample_code", sa.String(), nullable=True),
        sa.Column("data", postgresql.JSONB(), nullable=False),
    )
    op.create_index(
        "ix_submission_row_submission", "submission_row", ["submission_id", "row_number"]
    )
    op.create_index(
        "ix_submission_row_sample", "submission_row", ["submission_id", "sample_code"]
    )


def downgrade() -> None:
    op.drop_index("ix_submission_row_sample", table_name="submission_row")
    op.drop_index("ix_submission_row_submission", table_name="submission_row")
    op.drop_table("submission_row")
    for name, _ in _NEW_COLUMNS:
        op.drop_column("dataset_submission", name)

"""Stage the variables an uploader defines in the template's "New variables" sheet.

They are created in ``variables`` only when a reviewer approves the submission.

Revision ID: 0011_submission_new_variables
Revises: 0010_secondary_contact
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0011_submission_new_variables"
down_revision = "0010_secondary_contact"
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
    if "new_variables" not in existing:
        op.add_column(
            "dataset_submission",
            sa.Column("new_variables", postgresql.JSONB(), nullable=True),
        )


def downgrade() -> None:
    op.drop_column("dataset_submission", "new_variables")

"""Add a secondary contact to project_metadata.

A backup contact_name/contact_email, for when the primary contact doesn't
answer. Nullable — existing projects are unaffected.

Revision ID: 0010_secondary_contact
Revises: 0009_dataverse_metadata
"""

from alembic import op
import sqlalchemy as sa

revision = "0010_secondary_contact"
down_revision = "0009_dataverse_metadata"
branch_labels = None
depends_on = None

NEW_COLUMNS = [
    ("contact_name_2", sa.String()),
    ("contact_email_2", sa.String()),
]


def upgrade() -> None:
    bind = op.get_bind()
    existing = {
        r[0]
        for r in bind.execute(
            sa.text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name = 'project_metadata'"
            )
        )
    }
    for name, col_type in NEW_COLUMNS:
        if name not in existing:
            op.add_column("project_metadata", sa.Column(name, col_type, nullable=True))


def downgrade() -> None:
    for name, _ in NEW_COLUMNS:
        op.drop_column("project_metadata", name)

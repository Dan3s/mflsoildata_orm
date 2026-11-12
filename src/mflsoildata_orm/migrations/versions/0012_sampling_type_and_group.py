"""Add project_metadata.sampling_type and project_metadata.research_group.

sampling_type says how the soil was sampled: a JSON list of FARM_COMPOSITE and/or
SINGLE_POINT (a dataset can hold both);
research_group names the group, within the source organization, that produced
the data. Both nullable: existing projects are unaffected and the API/UI is what
asks for them on a new upload.

Revision ID: 0012_sampling_type_and_group
Revises: 0011_submission_new_variables
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0012_sampling_type_and_group"
down_revision = "0011_submission_new_variables"
branch_labels = None
depends_on = None

NEW_COLUMNS = [
    ("sampling_type", postgresql.JSONB()),
    ("research_group", sa.String()),
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

"""Add project_metadata columns for Dataverse-sourced metadata.

Supports importing datasets from Harvard Dataverse: authors, funding info,
language, related datasets, subject and geographic bounding box are fields
Dataverse's Citation/Geospatial metadata blocks carry that we did not have a
place for. All nullable — existing projects are unaffected.

Revision ID: 0009_dataverse_metadata
Revises: 0008_spatial_data_type
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

revision = "0009_dataverse_metadata"
down_revision = "0008_spatial_data_type"
branch_labels = None
depends_on = None

NEW_COLUMNS = [
    ("authors", JSONB()),
    ("funding_information", sa.Text()),
    ("language", sa.String()),
    ("related_datasets", JSONB()),
    ("subject", sa.String()),
    ("geographic_bounding_box", JSONB()),
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

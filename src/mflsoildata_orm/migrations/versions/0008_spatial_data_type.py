"""Add project_metadata.spatial_data_type.

Geometry the dataset describes (POINT | LINE | POLYGON | RASTER). Requested by
the data management team so a dataset can declare a geometry other than the
point sites the platform stores today.

Revision ID: 0008_spatial_data_type
Revises: 0007_submission_metadata
"""

from alembic import op
import sqlalchemy as sa

revision = "0008_spatial_data_type"
down_revision = "0007_submission_metadata"
branch_labels = None
depends_on = None


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
    if "spatial_data_type" not in existing:
        op.add_column("project_metadata", sa.Column("spatial_data_type", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column("project_metadata", "spatial_data_type")

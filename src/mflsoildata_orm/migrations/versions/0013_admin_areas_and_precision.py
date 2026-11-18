"""Admin-area gazetteer and the precision of a site's location.

A site no longer needs coordinates: with its admin 1 and admin 2 it is placed at the centre
of its area. ``sites.geom`` stays NOT NULL (every site has a point); what says how far to
trust it is the new ``sites.location_precision``: EXACT (coordinates given), ADMIN_2 or ADMIN_1
(the centre of that area). Existing sites are all EXACT.

``admin_areas`` is the reference those centres come from (loaded by the API's
``scripts/load_admin_areas.py``).

Revision ID: 0013_admin_areas_and_precision
Revises: 0012_sampling_type_and_group
"""

from alembic import op
import sqlalchemy as sa
import geoalchemy2

revision = "0013_admin_areas_and_precision"
down_revision = "0012_sampling_type_and_group"
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    insp = sa.inspect(bind)

    site_cols = {c["name"] for c in insp.get_columns("sites")}
    if "location_precision" not in site_cols:
        op.add_column(
            "sites",
            sa.Column("location_precision", sa.String(), nullable=False, server_default="EXACT"),
        )

    if "admin_areas" not in insp.get_table_names():
        op.create_table(
            "admin_areas",
            sa.Column("id", sa.BigInteger(), primary_key=True),
            sa.Column("iso3", sa.String(3), nullable=False),
            sa.Column("country", sa.String(), nullable=False),
            sa.Column("level", sa.SmallInteger(), nullable=False),
            sa.Column("name", sa.String(), nullable=False),
            sa.Column("name_norm", sa.String(), nullable=False),
            sa.Column("parent_name_norm", sa.String()),
            sa.Column(
                "centroid",
                geoalchemy2.Geometry(geometry_type="POINT", srid=4326, spatial_index=True),
                nullable=False,
            ),
            sa.Column("source", sa.String()),
            sa.Column(
                "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
            ),
        )
        op.create_index("ix_admin_areas_lookup", "admin_areas", ["iso3", "level", "name_norm"])


def downgrade() -> None:
    op.drop_index("ix_admin_areas_lookup", table_name="admin_areas")
    op.drop_table("admin_areas")
    op.drop_column("sites", "location_precision")

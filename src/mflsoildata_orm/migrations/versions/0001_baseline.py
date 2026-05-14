"""Baseline revision.

Revision ID: 0001_baseline
Revises: 
Create Date: 2026-05-13
"""
from alembic import op
import sqlalchemy as sa

# Import the SQLAlchemy metadata to create/drop tables
from mflsoildata_orm.database.base import Base


def upgrade() -> None:
    bind = op.get_bind()
    # Create all tables defined on Base.metadata. This is a simple baseline
    # migration that ensures the current models exist in the target DB.
    Base.metadata.create_all(bind=bind)


def downgrade() -> None:
    bind = op.get_bind()
    # Drop all tables created from the models. Use with caution in production.
    Base.metadata.drop_all(bind=bind)
"""Baseline revision.

Revision ID: 0001_baseline
Revises: 
Create Date: 2026-05-13
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_baseline"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

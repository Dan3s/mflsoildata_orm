from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func

from ..database.base import Base


class DownloadLog(Base):
    """Audit trail of data exports (RF32).

    Users live in Keycloak, so identity is stored denormalized (sub/email/username)
    rather than as a foreign key. ``filters`` is a JSON snapshot of the export
    request (projects, sites, variables, date range, matrix, include_metadata).
    """

    __tablename__ = "download_log"

    id = Column(BigInteger, primary_key=True)
    user_sub = Column(String)       # Keycloak subject id
    user_email = Column(String)
    username = Column(String)
    organization = Column(String)   # Keycloak user attribute (claim)
    country = Column(String)        # Keycloak user attribute (claim)
    format = Column(String, nullable=False)
    record_count = Column(BigInteger)
    filters = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

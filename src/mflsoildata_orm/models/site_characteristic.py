from sqlalchemy import BigInteger, Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class SiteCharacteristic(Base):
    __tablename__ = "site_characteristics"

    id = Column(BigInteger, primary_key=True)
    site_id = Column(
        BigInteger, ForeignKey("sites.id", ondelete="CASCADE"), nullable=False
    )
    profile_info = Column(JSONB)
    site_info = Column(JSONB)
    sampling_info = Column(JSONB)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    site = relationship("Site", back_populates="site_characteristics")

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class SampleTypeNote(Base):
    __tablename__ = "sample_type_notes"

    id = Column(BigInteger, primary_key=True)
    sample_id = Column(
        BigInteger, ForeignKey("samples.id", ondelete="CASCADE"), nullable=False
    )
    notes = Column(JSONB, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    sample = relationship("Sample", back_populates="type_notes")

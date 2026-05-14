from sqlalchemy import BigInteger, Column, DateTime, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from ..database.base import Base


class Method(Base):
    __tablename__ = "methods"

    id = Column(BigInteger, primary_key=True)
    method_code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    extractant = Column(String)
    description = Column(Text)
    notes = Column(JSONB)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    lab_batches = relationship("LabBatch", back_populates="method")

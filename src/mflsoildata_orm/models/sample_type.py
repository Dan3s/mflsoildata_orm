from sqlalchemy import BigInteger, Column, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from ..database.base import Base


class SampleType(Base):
    __tablename__ = "sample_types"

    id = Column(BigInteger, primary_key=True)
    sample_type_code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    notes = Column(JSONB)

    samples = relationship("Sample", back_populates="sample_type")

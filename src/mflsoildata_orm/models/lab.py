from sqlalchemy import BigInteger, Column, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from ..database.base import Base


class Lab(Base):
    __tablename__ = "labs"

    id = Column(BigInteger, primary_key=True)
    lab_code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    scope = Column(String)
    organization = Column(String)
    country = Column(String)
    notes = Column(JSONB)

    lab_batches = relationship("LabBatch", back_populates="lab")

from sqlalchemy import BigInteger, CheckConstraint, Column, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from ..database.base import Base


class Variable(Base):
    __tablename__ = "variables"
    __table_args__ = (
        CheckConstraint(
            "value_type IN ('numeric','text','boolean','date')",
            name="ck_variables_value_type",
        ),
    )

    id = Column(BigInteger, primary_key=True)
    variable_code = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    matrix = Column(String)
    value_type = Column(String, nullable=False)
    default_unit_id = Column(BigInteger, ForeignKey("units.id", ondelete="SET NULL"))
    description = Column(Text)
    notes = Column(JSONB)

    default_unit = relationship("Unit", back_populates="variables")
    measurements = relationship("Measurement", back_populates="variable")

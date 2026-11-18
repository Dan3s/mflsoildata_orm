from geoalchemy2 import Geometry
from sqlalchemy import BigInteger, Column, DateTime, Index, SmallInteger, String
from sqlalchemy.sql import func

from ..database.base import Base


class AdminArea(Base):
    """Reference gazetteer of administrative areas (level 1 = department/state, 2 = municipality).

    Lets a site that came without coordinates, but with its admin 1 and admin 2, be placed
    on the map at the centre of its area. ``centroid`` is a point that lies inside the area.
    Names are kept as given by the source and, normalised (lower case, no accents, no
    "Municipio de"…), in ``name_norm`` / ``parent_name_norm`` for matching.

    Filled by ``scripts/load_admin_areas.py`` of the API from geoBoundaries (CC BY 4.0).
    """

    __tablename__ = "admin_areas"
    __table_args__ = (Index("ix_admin_areas_lookup", "iso3", "level", "name_norm"),)

    id = Column(BigInteger, primary_key=True)
    iso3 = Column(String(3), nullable=False)
    country = Column(String, nullable=False)
    level = Column(SmallInteger, nullable=False)  # 1 or 2
    name = Column(String, nullable=False)
    name_norm = Column(String, nullable=False)
    parent_name_norm = Column(String)  # for level 2: the normalised name of its level-1 area
    centroid = Column(Geometry(geometry_type="POINT", srid=4326), nullable=False)
    source = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

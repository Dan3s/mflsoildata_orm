from sqlalchemy.orm import declarative_base
from . import engine

Base = declarative_base()


def create_tables() -> None:
    """
    Create all tables defined in SQLAlchemy models.
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("Tables created successfully.")
    except Exception as exc:
        print(f"Error creating tables: {exc}")
        raise

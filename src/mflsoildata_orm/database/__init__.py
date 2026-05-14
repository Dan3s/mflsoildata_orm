import os
from contextlib import contextmanager
from typing import Generator

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found in environment variables")


def _create_engine(database_url: str):
    if database_url.startswith("sqlite"):
        if ":memory:" in database_url or "mode=memory" in database_url:
            return create_engine(
                database_url,
                connect_args={"check_same_thread": False},
                poolclass=StaticPool,
            )
    return create_engine(database_url)


engine = _create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db() -> Generator[Session, None, None]:
    """
    Safe database session generator.
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError as exc:
        db.rollback()
        print(f"Database error: {exc}")
        raise
    except Exception as exc:
        db.rollback()
        print(f"Unexpected error: {exc}")
        raise
    finally:
        db.close()

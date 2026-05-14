"""
Alembic migrations for mflsoildata_orm.
"""
import os
from pathlib import Path

from alembic import command
from alembic.config import Config
from dotenv import load_dotenv


def get_alembic_config() -> Config:
    migrations_dir = Path(__file__).parent
    alembic_ini = migrations_dir.parent / "alembic.ini"

    config = Config(str(alembic_ini))
    config.set_main_option("script_location", str(migrations_dir))

    load_dotenv()
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        config.set_main_option("sqlalchemy.url", database_url)

    return config


def upgrade(revision: str = "head") -> None:
    config = get_alembic_config()
    command.upgrade(config, revision)
    print(f"Migrations upgraded to: {revision}")


def downgrade(revision: str) -> None:
    config = get_alembic_config()
    command.downgrade(config, revision)
    print(f"Migrations downgraded to: {revision}")


def current() -> None:
    config = get_alembic_config()
    command.current(config)


def history() -> None:
    config = get_alembic_config()
    command.history(config)


def stamp(revision: str = "head") -> None:
    config = get_alembic_config()
    command.stamp(config, revision)
    print(f"Database stamped at revision: {revision}")

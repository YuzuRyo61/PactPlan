import configparser

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read("alembic.ini")

PP_DB_ENGINE = create_engine(
    config["alembic"]["sqlalchemy.url"],
    echo=False
)

PP_DB_BASE = declarative_base()

PP_DB_SESSION = sessionmaker(
    bind=PP_DB_ENGINE
)


def create_all():
    PP_DB_BASE.metadata.create_all(PP_DB_ENGINE)

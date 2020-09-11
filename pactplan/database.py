import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import PP_CONFIG

PP_DB_ENGINE = create_engine(
    PP_CONFIG["database"]["uri"],
    echo=True
)

PP_DB_BASE = declarative_base()

PP_DB_SESSION = sessionmaker(
    bind=PP_DB_ENGINE
)


# noinspection PyUnresolvedReferences
def create_all():
    from . import models
    PP_DB_BASE.metadata.create_all(PP_DB_ENGINE)

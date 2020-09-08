import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from .config import PP_CONFIG

PP_DB = databases.Database(PP_CONFIG["database"]["uri"])

PP_DB_ENGINE = create_engine(
    PP_CONFIG["database"]["uri"],
    echo=True
)

PP_DB_BASE = declarative_base()


# noinspection PyUnresolvedReferences
def create_all():
    from . import models
    PP_DB_BASE.metadata.create_all(PP_DB_ENGINE)

from .database import PP_DB_SESSION


def db_session():
    try:
        database = PP_DB_SESSION()
        yield database
    finally:
        database.close()

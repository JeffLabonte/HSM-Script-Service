from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from contextlib import contextmanager
from functools import wraps
from threading import Lock


# BASE for schemas
BASE = declarative_base()

# TODO Change for some other DB at some point
_engine = create_engine('sqlite://script.sqlite', echo=True)
SessionFactory = sessionmaker(_engine)

sqlite_mutex = Lock()


@contextmanager
def get_session(auto_commit: bool = True) -> Session:
    with sqlite_mutex:
        session = SessionFactory()
        try:
            yield session
        except:
            if auto_commit:
                session.commit()
        finally:
            session.close()
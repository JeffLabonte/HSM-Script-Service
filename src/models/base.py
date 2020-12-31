from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


# TODO Change for some other DB at some point
ENGINE = create_engine('sqlite://script.sqlite', echo=True)

# BASE for schemas
BASE = declarative_base()

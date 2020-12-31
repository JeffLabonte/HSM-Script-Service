from sqlalchemy import Column, Integer, String

from models.base import BASE


class Scripts(BASE):
    __tablename__ = 'scripts'

    id = Column(Integer, primary_key=True)

from sqlalchemy import Column, Integer, String

from models.base import BASE


class Scripts(BASE):
    __tablename__ = 'scripts'

    id = Column(Integer, primary_key=True)
    name = Column("script_name", String(64))
    path = Column("script_path", String(256))

    def __repr__(self):
        return f"<Script(id={self.id}, name={self.name}, path={self.path})>"

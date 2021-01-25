from sqlalchemy import Column, Integer, String, relationship

from models.base import BASE


class GitRepository(BASE):
    id = Column(Integer, primary_key=True)
    repository = Column(String(256))


class Scripts(BASE):
    __tablename__ = 'scripts'

    id = Column(Integer, primary_key=True)
    name = Column("name", String(64))
    repository = relationship('GitRepository')
    exec = Column("exec", String(256))

    def __repr__(self):
        return f"<Script(id={self.id}, name={self.name}, path={self.path})>"

from sqlalchemy import *
from models.Base import Base

class Autor(Base):
    __tablename__ = 'autor'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    def __repr__(self):
        return "<Autor (nome='{0}')>".format(self.nome)

from sqlalchemy import *
from models.base import Base
from models.Livros import Livros


class Edicao(Base):
    __tablename__ = 'edicao'
    codigolivro = Column(Integer, ForeignKey('livros.codigo'))
    numero = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('codigolivro', 'numero'),
        {},
    )

    def __repr__(self):
        return "<Edicao(codigo='{0}', numero='{1}')>".format(self.codigolivro, self.numero)

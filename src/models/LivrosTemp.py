from sqlalchemy import *
from models.base import Base


class LivrosTemp(Base):
    __tablename__ = 'livrostemp'
    codigo = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    edicao = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return "<LivrosTemp(titulo='{0}')>".format(self.titulo)

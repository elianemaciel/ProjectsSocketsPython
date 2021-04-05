from sqlalchemy import *
from models.Base import Base
from models import Livros, Autor


class LivroAutor(Base):
    __tablename__ = 'livroautor'
    codigolivro = Column(Integer, ForeignKey('livros.codigo'), nullable=False)
    codigoautor = Column(Integer, ForeignKey('autor.codigo'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('codigolivro', 'codigoautor'),
        {},
    )

    def __repr__(self):
        return "<LivroAutor(cod_livro='{0}', cod_autor='{1}')>".format(self.codigolivro, self.codigoautor)

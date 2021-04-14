from sqlalchemy import *
from models.base import Base


class Livros(Base):
    __tablename__ = 'livros'

    codigo = Column(Integer, primary_key=True)
    titulo = Column(String)
   
    # Lets us print out a user object conveniently.
    def __repr__(self):
       return "<Livro(titulo='{0}')>".format(self.titulo)

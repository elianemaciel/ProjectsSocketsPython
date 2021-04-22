from sqlalchemy import *
from models.base import Base
from models import Livros, Autor
import json
from sqlalchemy.orm import relationship


class LivroAutor(Base):
    __tablename__ = 'livroautor'
    codigolivro = Column(Integer, ForeignKey('livros.codigo'), nullable=False)
    codigoautor = Column(Integer, ForeignKey('autor.codigo'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('codigolivro', 'codigoautor'),
        {},
    )

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<LivroAutor(cod_livro='{0}', cod_autor='{1}')>".format(self.codigolivro, self.codigoautor)

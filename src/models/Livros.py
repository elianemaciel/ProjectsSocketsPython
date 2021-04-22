from sqlalchemy import *
from models.base import Base
import json


class Livros(Base):
    __tablename__ = 'livros'

    codigo = Column(Integer, primary_key=True)
    titulo = Column(String)

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<Livro(titulo='{0}')>".format(self.titulo)

    def get_livros_infos(self, session):
        edition = session\
            .query(
                Livros.codigo,
                Livros.titulo,
                Edicao.numero,
                Edicao.ano,
            )\
            .join(Edicao)\
            .filter(Livros.codigo == self.codigo).first()

        ed_dict = {
            'titulo': edition.titulo,
            'edicao': edition.numero,
            'ano': edition.ano
        }
        return json.dumps(ed_dict)


class Edicao(Base):
    __tablename__ = 'edicao'
    codigolivro = Column(Integer, ForeignKey('livros.codigo'))
    numero = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('codigolivro', 'numero'),
        {},
    )

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<Edicao(codigo='{0}', numero='{1}')>".format(self.codigolivro, self.numero)

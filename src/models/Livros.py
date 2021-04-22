import json

from sqlalchemy import *
from models.base import Base

from sqlalchemy.orm import relationship, backref


class Edicao(Base):
    __tablename__ = 'edicao'
    codigolivro = Column(Integer, ForeignKey('livros.codigo', ondelete='cascade'))
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


class LivroAutor(Base):
    __tablename__ = 'livroautor'
    codigolivro = Column(Integer, ForeignKey('livros.codigo', ondelete='cascade'), nullable=False)
    codigoautor = Column(Integer, ForeignKey('autor.codigo', ondelete='cascade'), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('codigolivro', 'codigoautor'),
        {},
    )

    def to_json(self):
        return json.dumps(self.__dict__)

    @ classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<LivroAutor(cod_livro='{0}', cod_autor='{1}')>".format(self.codigolivro, self.codigoautor)


AUTOR_ID_SEQ = Sequence('autor_id_seq')  # define sequence explicitly


class Autor(Base):
    __tablename__ = 'autor'
    codigo = Column(Integer, AUTOR_ID_SEQ, primary_key=True, server_default=AUTOR_ID_SEQ.next_value())
    nome = Column(String, nullable=False)

    books_assoc = relationship(LivroAutor, backref="books_assoc", passive_deletes=True)

    def to_json(self):
        return json.dumps(self.__dict__)

    @ classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<Autor (nome='{0}')>".format(self.nome)


LIVROS_ID_SEQ = Sequence('livros_id_seq')  # define sequence explicitly


class Livros(Base):
    __tablename__ = 'livros'

    codigo = Column(Integer, LIVROS_ID_SEQ, primary_key=True, server_default=LIVROS_ID_SEQ.next_value())
    titulo = Column(String)

    authors = relationship(LivroAutor, backref="authors", passive_deletes=True)
    editions = relationship(Edicao, backref="editions", passive_deletes=True)

    def to_json(self):
        return json.dumps(self.__dict__)

    @ classmethod
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

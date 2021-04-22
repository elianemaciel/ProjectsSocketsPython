from sqlalchemy import *
from models.base import Base
import json


class LivrosTemp(Base):
    __tablename__ = 'livrostemp'
    codigo = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    edicao = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<LivrosTemp(titulo='{0}')>".format(self.titulo)

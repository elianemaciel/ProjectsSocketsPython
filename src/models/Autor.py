from sqlalchemy import *
from models.base import Base
import json


class Autor(Base):
    __tablename__ = 'autor'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)

    def to_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)

    def __repr__(self):
        return "<Autor (nome='{0}')>".format(self.nome)

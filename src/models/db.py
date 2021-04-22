import json
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine

from models import base, Autor, LivroAutor, Livros, LivrosTemp

with open('src/models/settings.json') as f:
    settings = json.load(f)
user, password, host, port, dbname = settings['db']['user'], settings['db'][
    'password'], settings['db']['host'], settings['db']['port'], settings['db']['dbname']

# The base class which our objects will be defined on.

connection_url = f'postgresql://{user}:{password}@{host}:{int(float(port))}/{dbname}'
print(connection_url)
engine = create_engine(connection_url, echo=True)

base.Base.metadata.create_all(engine, checkfirst=True)
# base.Base.query = db_session.query_property()

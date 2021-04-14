from sqlalchemy.sql import text
from models.db import engine
from sqlalchemy.orm import relationship, backref, sessionmaker

# Create all tables by issuing CREATE TABLE commands to the DB.
# Base.metadata.drop_all(engine) 
# Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()

files = [
    "src/models/scripts/livros.sql",
    "src/models/scripts/autor.sql",
    "src/models/scripts/edicao.sql",
    "src/models/scripts/livroautor.sql",
    "src/models/scripts/livrostemp.sql",
]
conn = engine.connect()


for item in files:
    trans = conn.begin()
    file = open(item)
    query = text(file.read())
    conn.execute(query)
    trans.commit()


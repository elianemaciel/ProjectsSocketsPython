from sqlalchemy.sql import text
from models.db import engine
from models.Base import Base

# Create all tables by issuing CREATE TABLE commands to the DB.
Base.metadata.drop_all(engine) 
Base.metadata.create_all(engine) 

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


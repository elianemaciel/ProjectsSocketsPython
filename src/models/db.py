import json
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine


with open('src/models/settings.json') as f:
    settings = json.load(f)
user, password, host, port, dbname = settings['db']['user'], settings['db']['password'], settings['db']['host'], settings['db']['port'], settings['db']['dbname']

connection_url =  f'postgresql://{user}:{password}@{host}:{int(float(port))}/{dbname}'
engine = create_engine(connection_url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(Session)

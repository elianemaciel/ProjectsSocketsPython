from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy.sql import text
from models.db import engine, db_session

# The base class which our objects will be defined on.
Base = declarative_base()
Base.query = db_session.query_property()



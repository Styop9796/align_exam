from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = 'sqlite:///./app.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False}
                       ) # create connection

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) # each connection to db will be SessionLocal object

Base = declarative_base() # base
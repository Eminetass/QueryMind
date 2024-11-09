from sqlalchemy import Column,Integer,String,DateTime,create_engine
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL =os.getenv('DATABASE_URL')
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

class Log(Base):
    __tablename__ = 'log'

    id = Column(Integer,primary_key=True,index=True)
    user_question = Column(String(500),nullable=False)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    assistant_answer = Column(String(500),nullable=False)
    DateTime = Column(DateTime(timezone=True),server_default=func.now())



from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer)
    position = Column(String, nullable=False)
    remote = Column(Boolean,default=True)
    #document_id = Column(String)


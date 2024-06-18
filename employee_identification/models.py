from .database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer)
    position = Column(String, nullable=False)
    remote = Column(Boolean,default=True)
    #document_id = Column(String)

"""
class Image(Base):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True)
    path = Column(String,nullable=False)
    employee_id = Column(Integer , ForeignKey('employees.id'))

    employee = relationship('Employee', back_populates='photo')
"""

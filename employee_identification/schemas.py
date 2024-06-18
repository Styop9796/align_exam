from pydantic import BaseModel
from typing import Optional
from fastapi import UploadFile,File

class EmployeeBase(BaseModel):
    first_name : str
    last_name : str
    age : int
    position : str
    remote : bool

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id : int
    image : str

    class Config:
        orm_mode : True



"""class ImageBase(BaseModel):
    image : UploadFile = File(...)

class ImageCreate(BaseModel):
    pass

class Image(ImageBase):
    id : int
    employee_id : int


    class Config:
        orm_mode= True"""

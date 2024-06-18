import os
from typing import Optional
from fastapi import FastAPI,Depends,HTTPException,Query
from sqlalchemy.orm import Session
from .database import engine,SessionLocal
from . import models ,schemas
from fastapi.templating import Jinja2Templates




app = FastAPI()

UPLOAD_DIR= 'images'
os.makedirs(UPLOAD_DIR,exist_ok=True)

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/employees/new/")
async def create_employee(
    employee: schemas.EmployeeBase ,
    db: Session = Depends(get_db)
):
    try:
        db_employee = models.Employee(
            first_name=employee.first_name,
            last_name=employee.last_name,
            age=employee.age,
            position=employee.position,
            remote=employee.remote,
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)

        return db_employee

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to create employee")


@app.get("/employees/list")
async def get_employees_list(
    name: Optional[str] = Query(None),
    position: Optional[str] = Query(None),
    remote: Optional[bool] = Query(None),
    db: Session = Depends(get_db)
):
    filters = {}
    if name:
        filters['first_name'] = name
    if position:
        filters['position'] = position
    if remote is not None:
        filters['remote'] = remote
    employees = db.query(models.Employee).filter_by(**filters).all()
    return employees


@app.get("/employees/{id}")
async def get_employee_by_id(id: int, db: Session = Depends(get_db)):
    db_employee = db.query(models.Employee).filter(models.Employee.id == id).first()
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee



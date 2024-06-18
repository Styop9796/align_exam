import os
from typing import Optional
from fastapi import FastAPI,Depends,UploadFile,File,Form,HTTPException,Query,Request
from sqlalchemy.orm import Session
from .database import engine,SessionLocal
from . import models ,schemas
from fastapi.templating import Jinja2Templates
from PIL import Image
import io
import pytesseract



templates = Jinja2Templates(directory="templates")
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def extract_text_from_image(image: Image.Image):
    text = pytesseract.image_to_string(image)
    cleaned_text = text.replace("\n",' ').replace('\f','')
    return cleaned_text


@app.get('/extract-text/')
async def extract_page(request: Request):
    return templates.TemplateResponse('add_employee.html',{"request":request})


@app.post("/extract-text/{employee_id}")
async def extract_text(employee_id:int , file: UploadFile = File(...)):
    try:
        text=''
        if file.content_type == 'image/png':
            image = Image.open(io.BytesIO(await file.read()))
            text = extract_text_from_image(image)
            print(text)

        return {"text":text}
    except Exception as e:
        print(e)
        return {'error': e}

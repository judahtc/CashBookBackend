from typing import List, Union

from fastapi import FastAPI, APIRouter,Depends
from application.Data import models,database, schemas
from application.Data.database import get_db
router=APIRouter( prefix="/entries",tags=["entries"])
from sqlalchemy.orm import Session
from application.CashBook import crud


@router.get("/")
def read_root():
    return {"Hello": "World"}


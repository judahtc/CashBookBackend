from typing import List, Union

from fastapi import FastAPI, APIRouter,Depends
from application.Data import models,database, schemas
from application.Data.database import get_db
router=APIRouter( prefix="/bills",tags=["bills"])
from sqlalchemy.orm import Session
from application.Bills import crud


@router.post("/add")
def create_bill(entries:schemas.BillRecordCreate,db:Session=Depends(get_db)):
    return crud.createBill(entry=entries,db=db)


@router.get("/read")
def read_bills(db: Session = Depends(get_db)):
    return crud.read_all_bills(db=db)

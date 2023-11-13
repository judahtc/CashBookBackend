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



@router.post("/add")
def create_entries(entries:schemas.CashbookEntryCreate,db:Session=Depends(get_db)):
    return crud.createEntry(entry=entries,db=db)

@router.get("/read", response_model=List[schemas.CashbookEntry])
def read_cashbook_entries(db: Session = Depends(get_db)):
    return crud.read_all_entries(db=db)

@router.get("/read/{id}")
def read_entry(id:str,db: Session = Depends(get_db))->Union[schemas.CashbookEntryBase,None]:
    return crud.read_entry_by_id(db=db,id=id)


@router.delete("/read/{id}")
def delete_entry(id:str,db: Session = Depends(get_db)):
    return crud.delete_entry_by_id(db=db,id=id)




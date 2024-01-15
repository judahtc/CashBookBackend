from typing import List, Union

from fastapi import FastAPI, APIRouter,Depends,HTTPException
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


@router.post("/add_bill/{record_id}")
async def add_bill(record_id: int, bill: schemas.BillAdd,db: Session = Depends(get_db)):
   
    record = db.query(models.Bills).filter(models.Bills.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    # Update the JSONB column with the new bills dictionary
    existing_bills = record.bills or {}  # Handle the case where record.bills is None
    existing_bills = {**existing_bills, **bill.bills}


    record.bills = existing_bills
    db.commit()
    db.refresh(record)

    db.close()
    return record
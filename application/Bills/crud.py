from application.Data import models,schemas
from typing import *
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session

from sqlalchemy import create_engine, Column, Float, func


def createBill(entry: schemas.CashbookEntryCreate, db: Session):
        record = models.Bills(**entry.dict())
        db.add(record)
        db.commit()
        db.refresh(record)

        db.close()
        return record

def read_all_bills(db:Session):
    return db.query(models.Bills).all()
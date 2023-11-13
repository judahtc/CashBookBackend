from application.Data import models,schemas
from typing import *
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session


def createEntry(entry: schemas.CashbookEntryCreate, db: Session):
    # Create a new CashbookEntry instance
    new_entry = models.CashbookEntry(
        amount=entry.amount,
        rate=entry.rate,
        category=entry.category,
        description=entry.description,
        payment_mode=entry.payment_mode,
        user_id='1',
        business_id='1'
    )

    # Add the new entry to the session
    db.add(new_entry)

    # Commit the transaction to make the new entry persistent in the session
    db.commit()

    # Refresh the new_entry after committing
    db.refresh(new_entry)

    return {"response": "Entry successfully created"}

def read_all_entries(db:Session):
    return db.query(models.CashbookEntry).all()

def read_entry_by_id(db:Session,id:str):
    try:
        return db.query(models.CashbookEntry).filter(models.CashbookEntry.id==id).first()
    except NoResultFound:
        raise Exception(f"Entry with id {id} not found")
def delete_entry_by_id(db:Session,id:str):
    try:
        entry= db.query(models.CashbookEntry).filter(models.CashbookEntry.id==id).first()
        db.delete(entry)
        db.commit()

        return {"response":"file successfully deleted"}
    except NoResultFound:
        raise Exception(f"Entry with id {id} not found")
    

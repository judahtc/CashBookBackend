from datetime import datetime
from pydantic import BaseModel

class CashbookEntryBase(BaseModel):
    created_date: str
    payment_mode: str
    category: str
    amount: float
    rate: float
   
    description: str
   

    class Config:
        orm_mode = True

class CashbookEntryCreate(BaseModel):
    amount: float
    rate: float
    payment_mode: str
    category: str
    description: str
    
    class Config:
        orm_mode = True


class CashbookEntry(CashbookEntryBase):


    class Config:
        orm_mode = True
from typing import Dict


class BillRecordCreate(BaseModel):
    month: str
    bills: Dict[str, float]

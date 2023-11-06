from datetime import datetime
from pydantic import BaseModel

class CashbookEntryBase(BaseModel):
    user_id: str
    business_id: str
    amount: float
    rate: float
    payment_mode: str
    category: str
    description: str
    created_date: str

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
    id: int

    class Config:
        orm_mode = True

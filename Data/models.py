from datetime import datetime
from enum import Enum

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import Enum as SQLAlchemyEnum


from Data.database import Base

class CashbookEntry(Base):
    __tablename__ = "cashbook_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String)
    business_id = Column(String)
    amount = Column(Float)
    rate = Column(Float)
    payment_mode = Column(String)
    category = Column(String)
    description = Column(String)
    created_date= Column(String,default=datetime.now())
    updated_date= Column(String,default=datetime.now())
    void=Column(String,default=False)
    void_date=Column(String,default=None)



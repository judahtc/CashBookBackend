from typing import Union
from mangum import Mangum
from fastapi import FastAPI
from application.Data.database import  SessionLocal, engine, get_db
from application.Data import database, models, schemas
from application.CashBook import entries
from application.Bills import bills
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
handler = Mangum(app)

database.Base.metadata.create_all(bind=engine)

@app.get("/health")
def read_root():
    return {"Hello": "World"}
@app.get("/")
def read_root():
    return {"Hello": "Welcome to your CASHBOOK application"}

app.include_router(entries.router)
app.include_router(bills.router)

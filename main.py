from typing import Union

from fastapi import FastAPI
from Data.database import  SessionLocal, engine, get_db
from Data import database, models, schemas
from CashBook import entries
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database.Base.metadata.create_all(bind=engine)

@app.get("/health")
def read_root():
    return {"Hello": "World"}

app.include_router(entries.router)

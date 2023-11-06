from typing import Union

from fastapi import FastAPI
from CashBook import entries
app = FastAPI()


@app.get("/health")
def read_root():
    return {"Hello": "World"}

app.include_router(entries.router)

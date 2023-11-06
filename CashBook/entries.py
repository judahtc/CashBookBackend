from typing import Union

from fastapi import FastAPI, APIRouter

router=APIRouter( prefix="/entries",tags=["entries"])

@router.get("/")
def read_root():
    return {"Hello": "World"}


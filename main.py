from fastapi import FastAPI
from typing import List, Union
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    color: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/items")
async def read_item_list() -> List[Item]:
    my_item: Item = Item(name="nolan", id=1, color="green")
    return [my_item]

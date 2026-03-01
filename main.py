from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str = None
    is_done: bool = False

items = []

@app.get("/")
def root():
    return {"message": "Hello World!"}

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items

@app.get("/items", response_model=list[Item])
def get_items(limit: int = 10) -> list:
    return items[:limit]

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: str) -> Item:
    if int(item_id) >= len(items) or int(item_id) < 0:
        raise HTTPException(status_code=404, detail="Item not found")

    item = items[int(item_id)]
    return item
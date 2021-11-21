from fastapi import FastAPI, status, HTTPException
from Item import Item

app = FastAPI()

items = []


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")  # passing the id as a parameter in the path
async def read_item(item_id: int):
    try:
        return items[item_id]  # Looks for the index of item in your dataset and attempts to return it.
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")  # Returns a 404 error not found if not in dataset


@app.get('/items')  # Gets all the items in the data set.
async def all_items():
    return items


@app.get("/meaning_of_life")  # passing the id as a parameter in the path
async def meaning_of_life():
    return 42


@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):  # Creating an item that would prosumably be in the body of the request
    item.id = len(items)
    items.append(item)
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_202_ACCEPTED)
async def remove_item(item_id: int):
    try:
        del items[item_id]  # remove the item from the data set.
        return {"detail": "item removed"}
    except IndexError:
        raise HTTPException(status_code=400,
                            detail="Item not deleted")  # Returns a 404 error not found if not in dataset

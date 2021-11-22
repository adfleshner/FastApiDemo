from fastapi import FastAPI, status, HTTPException
from Item import Item
from DataStoreInterface import LocalDataStore

app = FastAPI()
ds = LocalDataStore()

@app.get("/")
async def root():  # The Root of the porject.
    return {"message": "Hello World"}


@app.get("/items/{item_id}")  # passing the id as a parameter in the path
async def read_item(item_id: int):
    try:
        return ds.get_item(item_id)  # Looks for the index of item in your dataset and attempts to return it.
    except IndexError:
        raise HTTPException(status_code=404, detail="Item not found")  # Returns a 404 error not found if not in dataset


@app.get('/items')  # Gets all the items in the data set.
async def all_items():
    return ds.get_all_items()


@app.get("/meaning_of_life")  # passing the id as a parameter in the path
async def meaning_of_life():
    return 42


@app.post("/items", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):  # Creating an item that would prosumably be in the body of the request
    ds.add_item(item)
    return item


@app.delete("/items/{item_id}", status_code=status.HTTP_202_ACCEPTED)
async def remove_item(item_id: int):
    try:
        ds.remove_item(item_id)  # remove the item from the data set.
        return {"detail": "item removed"}
    except IndexError:
        raise HTTPException(status_code=400,
                            detail="Item not deleted")  # Returns a 404 error not found if not in dataset

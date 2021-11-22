from fastapi import FastAPI, status, HTTPException
from Item import Item
from DataStoreInterface import LocalDataStore

app = FastAPI()
ds = LocalDataStore()


@app.get("/")
async def root():  # The Root of the project.
    return {"message": "Hello World"}


@app.get("/items/{item_id}")  # passing the id as a parameter in the path
async def read_item(item_id: int):
    try:
        item = ds.get_item(item_id)
        if item is None:  # raise an IndexError if a null is returned from the ds
            raise IndexError
        return item  # Looks for the index of item in your dataset and attempts to return it.
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
    try:
        ds.add_item(item)
        return item
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Item not added")


@app.delete("/items/{item_id}", status_code=status.HTTP_202_ACCEPTED)
async def remove_item(item_id: int):
    try:
        removed_item = ds.remove_item(item_id)  # remove the item from the data set.
        if removed_item is None:  # raise an IndexError if a null is returned from the ds
            raise IndexError
        return removed_item
    except IndexError:
        raise HTTPException(status_code=400,
                            detail="Item not deleted")  # Returns a 404 error not found if not in dataset

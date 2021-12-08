from fastapi import FastAPI, status, HTTPException
from item import Item
from data_store import LocalDataStore
from local_paged_store import LocalPagedStore
from PagedItem import PagedItem
from random import randint

app = FastAPI()
ds = LocalDataStore()

pds = LocalPagedStore()


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


@app.post("/paged/item", status_code=status.HTTP_201_CREATED)
async def create_paged_item(item: PagedItem):
    try:
        pds.add_item(item.name)
        return item
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Item not added")


@app.delete("/paged/items/all", status_code=status.HTTP_202_ACCEPTED)
async def delete_all_paged_items():
    pds.clear_all_items()
    return "Cleared all items"


@app.post("/paged/item/amount/{number}", status_code=status.HTTP_201_CREATED)
async def create_paged_item_of_amount(item: PagedItem, number: int):
    try:
        org_item = item
        for _ in range(number):
            pds.add_item(org_item.name + f" {randint(0,1_000_000)}")
        return f"{number} of items created"
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Not Allowed")


@app.get("/paged/items/all")
async def get_paged_items():
    all_paged = pds.get_all_items()
    return all_paged


@app.get("/paged/items/offset/{offset}/limit/{limit}")
async def get_paged_items(offset: int, limit: int):
    all_paged = pds.get_items_paged(limit, offset)
    return all_paged

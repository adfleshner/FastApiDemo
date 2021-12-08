from sqlite3 import Row, Cursor
from typing import Optional
from pydantic import BaseModel


def cursor_to_item(cursor: Cursor, row: Row):
    d = {}
    item = row
    for idx, col in enumerate(cursor.description):
        d[col[0]] = item[idx]
    return d


class PagedItem(BaseModel):
    id: Optional[int] = None
    name: str

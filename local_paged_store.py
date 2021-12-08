import sqlite3 as sl
from PagedItem import PagedItem, cursor_to_item


# class to handle all database operations
class LocalPagedStore:
    # connect to the database
    con = sl.connect('fast_api_db_paged.db')
    # name of the items table
    items_table_name = "PAGED_ITEMS"

    # Creates a new Database
    def __init__(self):
        create_table_sql = f"""
                CREATE TABLE IF NOT EXISTS {self.items_table_name} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                );
            """
        self.con.execute(create_table_sql)

    # Get all items from the database and returning them as a list.
    # Each row that is returned is set to a dictionary.
    def get_all_items(self):
        get_all_items_sql = f"""SELECT * FROM {self.items_table_name};"""
        data = self.con.execute(get_all_items_sql)
        items = []
        for row in data:
            items.append(cursor_to_item(data, row))
        self.con.commit()
        return items

    def get_first_id(self):
        first_item = f"""SELECT * FROM {self.items_table_name} LIMIT 1;"""
        data = self.con.execute(first_item)
        items = []
        for row in data:
            items.append(cursor_to_item(data, row))
        self.con.commit()
        return items[0]['id']

    def get_items_paged(self, limit, after):
        first_id = self.get_first_id()
        start = first_id + after
        get_items_from_to_sql = f"""SELECT * FROM {self.items_table_name} 
                                    WHERE id > {start} 
                                    LIMIT {limit};"""
        data = self.con.execute(get_items_from_to_sql)
        items = []
        for row in data:
            items.append(cursor_to_item(data, row))
        self.con.commit()
        return items

    # Inserting a new item into the DB
    def add_item(self, item: str):
        insert_table_sql = f"""INSERT INTO {self.items_table_name} (name)
                VALUES ('{item}');"""
        self.con.execute(insert_table_sql)
        self.con.commit()

    # Getting an item from the DB if it is available.
    def get_item(self, item_id: int):
        get_item_at_id_sql = f"""SELECT * FROM {self.items_table_name} WHERE id={item_id};"""
        cursor = self.con.execute(get_item_at_id_sql)
        try:
            return cursor_to_item(cursor, cursor.fetchone())
        except TypeError:
            return None

    def clear_all_items(self):
        clear_table_sql = f"""DELETE FROM {self.items_table_name}"""
        self.con.execute(clear_table_sql)
        self.con.commit()




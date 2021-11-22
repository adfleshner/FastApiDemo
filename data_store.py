import sqlite3 as sl
from item import Item, cursor_to_item


# class to handle all database operations
class LocalDataStore:
    # connect to the database
    con = sl.connect('fast_api_db.db')
    # name of the items table
    items_table_name = "ITEMS"

    # Creates a new Database
    def __init__(self):
        create_table_sql = f"""
                CREATE TABLE IF NOT EXISTS {self.items_table_name} (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    description TEXT,
                    price FLOAT,
                    tax FLOAT
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

    # Getting an item from the DB if it is available.
    def get_item(self, item_id: int):
        get_item_at_id_sql = f"""SELECT * FROM {self.items_table_name} WHERE id={item_id};"""
        cursor = self.con.execute(get_item_at_id_sql)
        try:
            return cursor_to_item(cursor, cursor.fetchone())
        except TypeError:
            return None

    # Inserting a new item into the DB
    def add_item(self, item: Item):
        insert_table_sql = f"""INSERT INTO {self.items_table_name} (name, description, price, tax)
                VALUES ('{item.name}', '{item.description}', {item.price}, {item.tax});"""
        self.con.execute(insert_table_sql)
        self.con.commit()

    # Deletes an item from the database and returns it if it is available.
    # Otherwise returns None.
    def remove_item(self, item_id: int):
        item_to_remove = self.get_item(item_id)
        if item_to_remove is not None:  # checking if the item that you want to remove is valid
            delete_from_table_sql = f"""DELETE FROM {self.items_table_name}  WHERE id={item_id};"""
            self.con.execute(delete_from_table_sql)
            self.con.commit()
        return item_to_remove  # returning that item that has just deleted.

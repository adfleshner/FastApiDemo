import sqlite3 as sl
from Item import Item


class LocalDataStore:

    con = sl.connect('fast_api_db.db')
    items_table_name = "ITEMS"

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

    def get_all_items(self):
        get_all_items_sql = f"""SELECT * FROM {self.items_table_name};"""
        data = self.con.execute(get_all_items_sql)
        items = []
        for row in data:
            items.append(row)
        return items

    def get_item(self, item_id: int):
        get_item_at_id_sql = f"""SELECT * FROM {self.items_table_name} WHERE id={item_id};"""
        return self.con.execute(get_item_at_id_sql)

    def add_item(self, item: Item):
        insert_table_sql = f"""INSERT INTO {self.items_table_name} (name, description, price, tax)
                VALUES ('{item.name}', '{item.description}', {item.price}, {item.tax});"""
        self.con.execute(insert_table_sql)
        return self.con.commit()

    def remove_item(self, item_id: int):
        delete_from_table_sql = f"""DELETE FROM {self.items_table_name}  WHERE id={item_id};"""
        self.con.execute(delete_from_table_sql)
        return self.con.commit()
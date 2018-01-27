import sqlite3
from functools import reduce

from table import *


DATABASE_CHEMIST = "chemist.sqlite"
TABLE_PRICE = "price"
COLUMN_ID = 'id'
COLUMN_DATE = 'date'
COLUMN_PRICE = 'price'
COLUMN_SAVE = 'save'
COLUMNS = [COLUMN_ID, COLUMN_DATE, COLUMN_PRICE, COLUMN_SAVE]


class PriceTable(Table):
    def __init__(self, conn):
        super(PriceTable, self).__init__(conn, TABLE_PRICE)

    def create_tbl(self):
        cur = self.conn.cursor()
        cur.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.name}
            (
                {COLUMN_ID} integer,
                {COLUMN_DATE} integer,
                {COLUMN_PRICE} real,
                {COLUMN_SAVE} real
            );
        
        
        ''')
        cur.close()

    def productHasSamePriceWithLastEntry(self, id, price):
        result = self.fetchall(f"id={id}")
        if not len(result):
            return False
        last_entry = reduce(lambda x, y: x if x['date'] > y['date'] else y, result, result[0])
        return abs(last_entry['price'] - price) < 0.01


if __name__ == '__main__':
    conn = sqlite3.connect(DATABASE_CHEMIST)
    price = PriceTable(conn)

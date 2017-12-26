import sqlite3


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



if __name__ == '__main__':
    conn = sqlite3.connect(DATABASE_CHEMIST)
    price = PriceTable(conn)
    print(price.description())
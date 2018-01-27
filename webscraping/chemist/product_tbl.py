from table import *

DATABASE_CHEMIST = "chemist.sqlite"
TABLE_PRODUCT = "product"
COLUMN_NAME = 'name'
COLUMN_ID = 'id'
COLUMN_URL = 'url'
COLUMN_OVERVIEW = 'overview'

COLUMNS = [COLUMN_ID, COLUMN_NAME, COLUMN_OVERVIEW, COLUMN_URL]



class ProductTable(Table):
    def __init__(self, conn):
        super(ProductTable, self).__init__(conn, TABLE_PRODUCT)



if __name__ == '__main__':
    pass
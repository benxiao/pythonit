from table import *

DATABASE_CHEMIST = "chemist.sqlite"
TABLE_ADDEDDATE = "date_added"
COLUMN_ID = 'id'
COLUMN_TIMESTAMP = 'time_stamp'
COLUMN_TIMESTAMPSTRING = 'ts_string'
COLUMNS = [COLUMN_ID, COLUMN_TIMESTAMP, COLUMN_TIMESTAMPSTRING]


class OperationDateTable(Table):
    def __init__(self, conn):
        super(OperationDateTable, self).__init__(conn, TABLE_ADDEDDATE)



    def largest_id(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT MAX(id) from {TABLE_ADDEDDATE}")
        cur.row_factory = None
        ret = cur.fetchone()
        cur.close()
        return ret[0] if ret else 0


if __name__ == '__main__':
    pass
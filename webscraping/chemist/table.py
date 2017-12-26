class UnknownColumn(Exception):
    pass


class ReadOnlyMode(Exception):
    pass


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Table:
    def __init__(self, conn, tbl):
        self.conn = conn
        self.conn.row_factory = dict_factory
        self.inWriteMode = False
        self.tbl = tbl
        self.cols = self.description()

    def description(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM {}".format(self.tbl))
        cur.row_factory = None
        result = [row[0] for row in cur.description]
        cur.close()
        return result

    def __len__(self):
        stmt = "SELECT count(*) FROM {};".format(self.tbl)
        cur = self.conn.cursor()
        cur.execute(stmt)
        cur.row_factory = None
        return cur.fetchone()[0]

    def delete(self, i):
        if not self.inWriteMode:
            raise ReadOnlyMode()
        cur = self.conn.cursor()
        stmt = "DELETE FROM {} WHERE id = ?"
        cur.execute(stmt.format(self.tbl), i)
        cur.close()

    def _insert(self, content):
        columns = []
        values = []
        for key, value in content.items():
            if key not in self.cols:
                raise UnknownColumn(key)
            columns.append(key)
            values.append(value)

        columns_part = ",".join(columns)
        values_part = ",".join("?" for _ in range(len(columns)))
        stmt = """INSERT INTO {} ({}) VALUES ({});""".format(self.tbl,
                                                             columns_part,
                                                             values_part)
        cur = self.conn.cursor()
        cur.execute(stmt, values)
        cur.close()

    def insert_many(self, iter_content):
        for content in iter_content:
            self._insert(content)

    def insert(self, content):
        if not self.inWriteMode:
            raise ReadOnlyMode()
        self._insert(content)

    def update(self, id, content):
        if not self.inWriteMode:
            raise ReadOnlyMode()
        columns = []
        values = []
        for key, value in content.items():
            if key not in self.cols:
                raise UnknownColumn(key)
            columns.append(key)
            values.append(value)
        columns_part = ','.join(str(k)+"= ?" for k in content)
        stmt = """UPDATE {} SET {} WHERE id = {};""".format(self.cols,
                                                           columns_part,
                                                           id)
        cursor = self.conn.cursor()
        cursor.execute(stmt, content)
        cursor.close()

    def __enter__(self):
        self.inWriteMode = True
        return self

    def __exit__(self, *args):
        self.inWriteMode = False
        self.conn.commit()

    def rows(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * from {}".format(self.tbl))
        result = list(cur.fetchall())
        cur.close()
        return result

    def __getitem__(self, i):
        cur = self.conn.cursor()
        cur.execute("SELECT * from {} where id = {};".format(self.tbl, i))
        result =  cur.fetchone()
        cur.close()
        return result

    def commit_change(self):
        self.conn.commit()

class UnknownColumn(Exception):
    pass


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class Table:
    def __init__(self, conn, name):
        self.conn = conn
        self.conn.row_factory = dict_factory
        self.readOnly = False
        self.name = name
        self.columns = self._columns()

    def _columns(self):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM {self.name};")
        cur.row_factory = None
        result = [row[0] for row in cur.description]
        cur.close()
        return result

    def __len__(self):
        stmt = f"SELECT count(*) FROM {self.name};"
        cur = self.conn.cursor()
        cur.execute(stmt)
        cur.row_factory = None
        result = cur.fetchone()[0]
        cur.close()
        return result

    def _fetch(self, conditions):
        cur = self.conn.cursor()
        stmt = f"SELECT * FROM {self.name} where {conditions}"
        try:
            cur.execute(stmt)
            return cur
        except:
            return None

    def fetchone(self,conditions):
        cur = self._fetch(conditions)
        if cur:
            return cur.fetchone()

    def fetchall(self, conditions):
        cur = self._fetch(conditions)
        if cur:
            return cur.fetchall()

    def insert(self, content):
        try:
            columns = []
            values = []
            for key, value in content.items():
                if key not in self.columns:
                    raise UnknownColumn(key)
                columns.append(key)
                values.append(value)

            columns_part = ",".join(columns)
            values_part = ",".join("?" for _ in range(len(columns)))
            stmt = f'''INSERT INTO {self.name} ({columns_part}) VALUES ({values_part});'''
            cur = self.conn.cursor()
            cur.execute(stmt, values)
            cur.close()
            return True

        except:
            return False

    def call(self, callback):
        cur = self.conn.cursor()
        result = callback(cur)
        cur.close()
        return result

    def insert_many(self, iter_content):
        for content in iter_content:
            self.insert(content)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.conn.commit()

    def rows(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * from {}".format(self.name))
        result = list(cur.fetchall())
        cur.close()
        return result

    def commit_change(self):
        self.conn.commit()

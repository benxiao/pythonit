from datetime import datetime
import time
import sqlite3

import chemist_soup
import price_tbl
import product_tbl
import date_tbl
from product_tbl import ProductTable
from price_tbl import PriceTable
from date_tbl import AddedDateTable

A_DAY = 86400


def main():
    conn = sqlite3.connect("chemist.sqlite")
    with PriceTable(conn) as t_price, \
         ProductTable(conn) as t_product, \
         AddedDateTable(conn) as t_date:

        last = t_date.last_date()
        if last:
            gap = datetime.now() - last
            print("{}s".format(gap.total_seconds()))
            if gap.total_seconds() / A_DAY < 2:
                print("last update is less than a day old.")
                return

        t_date.insert({date_tbl.COLUMN_TIMESTAMP: int(time.time()), date_tbl.COLUMN_TIMESTAMPSTRING: str(
             datetime.now())})
        t_date.commit_change()

        date_id = t_date.largest_id()
        print(date_id)
        data = t_product.rows()
        name2id = {row[product_tbl.COLUMN_NAME]: row[product_tbl.COLUMN_ID] for row in data}
        products = chemist_soup.download_data()
        for p in products:
            if not name2id.get(p.name):
                name2id[p.name] = len(t_product)
                t_product.insert({product_tbl.COLUMN_NAME: p.name})
                t_product.commit_change()

            t_price.insert({price_tbl.COLUMN_ID: name2id[p.name],
                              price_tbl.COLUMN_DATE: date_id,
                              price_tbl.COLUMN_PRICE: p.price,
                              price_tbl.COLUMN_SAVE: p.save})


    conn.close()

if __name__ == '__main__':
    main()


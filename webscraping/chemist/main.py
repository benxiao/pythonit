from datetime import datetime
import time
import sqlite3
import chemist_soup
import price_tbl
import product_tbl
import date_tbl
from product_tbl import ProductTable
from price_tbl import PriceTable
from date_tbl import OperationDateTable


def main():
    conn = sqlite3.connect("/home/ranxiao/pythonit/webscraping/chemist/chemist.sqlite")
    with PriceTable(conn) as t_price, \
         ProductTable(conn) as t_product, \
         OperationDateTable(conn) as t_date:

        t_date.insert({date_tbl.COLUMN_TIMESTAMP: int(time.time()), date_tbl.COLUMN_TIMESTAMPSTRING: str(
             datetime.now())})
        t_date.commit_change()

        date_id = t_date.largest_id()
        data = t_product.rows()
        name2id = {row[product_tbl.COLUMN_NAME]: row[product_tbl.COLUMN_ID] for row in data}
        products = chemist_soup.download_data()
        for p in products:
            if not name2id.get(p.name):
                name2id[p.name] = len(name2id)
                t_product.insert({product_tbl.COLUMN_NAME: p.name})

            if not t_price.productHasSamePriceWithLastEntry(name2id[p.name], p.price):
                t_price.insert({price_tbl.COLUMN_ID: name2id[p.name],
                              price_tbl.COLUMN_DATE: date_id,
                              price_tbl.COLUMN_PRICE: p.price,
                              price_tbl.COLUMN_SAVE: p.save})

    conn.close()


main()

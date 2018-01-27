from bs4 import BeautifulSoup
import requests
from multiprocessing.pool import Pool
from enum import Enum
CHEMIST_HOME = "https://www.chemistwarehouse.com.au/shop-online/81/vitamins?page={}"


class Supplement:
    def __init__(self):
        self.name = None
        self.date = None
        self.price = None
        self.save = 0
        self.overview = None
        self.url = None

    def __str__(self):
        return self.name+" P:"+str(self.price)+" S:"+str(self.save)+" R:"+str(int(self.discount() * 100)) + "%"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return str(self) == str(other)

    def discount(self):
        return round(self.save/(self.save+self.price),3) if self.save else 0


    __repr__ = __str__


def get_number_of_page():
    url = CHEMIST_HOME.format(1)
    resp = requests.get(url)
    if not resp.ok:
        print("warn {} failed".format(url))
    soup = BeautifulSoup(resp.content, features="html.parser")
    try:
        url = soup.find(name='a', attrs={"class":'last-page'}).get('href')
        i = url.find('page=')
        if i != -1:
            return int(url[i:].split('=')[1])
    except:
        pass

supplements = set()
def get_supplement_on_page(n):
    url = CHEMIST_HOME.format(n)
    resp = requests.get(url)
    if not resp.ok:
        print("warn {} failed".format(url))
    soup = BeautifulSoup(resp.content, features="html.parser")
    for tag in soup.findAll(name='a', attrs={'class': "product-container"}):
        sup = Supplement()
        try:
            sup.url = tag.get('href')
        except:
            pass

        try:
            sup.name = tag.get("title")
        except:
            pass

        try:
            price_tag = tag.find(name='span', attrs={"class": "Price"}).text.strip()
            if price_tag[0] == "$":
                sup.price = float(price_tag[1:])
        except:
            pass

        try:
            save_tag = tag.find(name='span', attrs={"class": "Save"}).text.strip()
            if save_tag.startswith("SAVE"):
                sup.save = float(save_tag.split()[1][1:])
        except:
            pass

        if sup.name and sup.price:
            supplements.add(sup)

    return supplements


def search(products, search_terms, n=30, sortBy=None):
    """
    :param products:
    :param search_terms:
    :param n:
    :param sortBy:
    :return:
    """
    lst = list(products)
    assert not isinstance(search_terms, str)
    for a in search_terms:
        lst = list(filter(lambda x: a.upper() in x.name.upper(), lst))
    bySave = lambda x: x.save if x.save else 0
    byDiscount = lambda x: x.discount()
    sortBy = bySave if not sortBy else byDiscount
    lst.sort(key=sortBy, reverse=True)
    result = lst[:n]
    for i, p in enumerate(result):
        print(i, ":", p)
    return result


def download_data():
    pool = Pool(8)
    results = pool.map(get_supplement_on_page, list(range(1, get_number_of_page()+1)))
    products = set()
    # sorted by the biggest discount

    for s in results:
        products = products.union(s)
    return list(products)


if __name__ == '__main__':

    import time
    from product_tbl import *
    # start = time.time()

    # lst = searc







import asyncio
import aiohttp
from bs4 import BeautifulSoup
import time
from sys import stderr
from asyncio import Queue
from functools import reduce
import aiofiles

# globals
HOME = "https://en.wikipedia.org"
tasks = Queue()
edges = Queue()
seen = set()
edgeLimit = 300_000
nEdges = 0
loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop, connector=aiohttp.TCPConnector(verify_ssl=False))
out = None
subject = "Cris_Cyborg"


async def init():
    global out
    await tasks.put(f"/wiki/{subject}")
    out = await aiofiles.open(f"{subject.lower()}.txt", "w")


async def get_page(url):
    async with client.get(url) as resp:
        if resp.status != 200:
            return
        return await resp.read()


def get_urls(page):
    soup = BeautifulSoup(page, features="html.parser")
    ps = soup.findAll("p")[:5]
    c0 = lambda x: x.get("title") is not None  # contain "title attribute
    c1 = lambda x: x.get("class") is None  # does not contain class attribute
    c2 = lambda x: x.get("href").count('\\') <= 2  # does not contain more than two backslashes
    c3 = lambda x: all(map(lambda x0: x0.isalpha(), get_title_from_link(x.get('href')).split("_")))  # title only
    try:
        #  contains English characters and underscore
        links = list(filter(lambda x: c0(x) and c1(x) and c2(x) and c3(x),
                            reduce(lambda x, y: x + y.findAll("a"), ps, [])))

        return [x.get("href") for x in links]
    except Exception as err:
        print("bs4 error", err, file=stderr)
        return []


def get_title_from_link(url):
    # grab the title from the partial link
    return url[url.rfind("/") + 1:]


def get_edges(url, urls):
    return [get_title_from_link(url) + "->" + get_title_from_link(x) for x in urls]


async def worker(id):
    while 1:
        url = await tasks.get()
        # print(url, id)
        try:
            page = await get_page(HOME + url)
        except Exception as err:
            print("get_page", err, file=stderr)
            continue

        if not page:
            continue

        urls = [x for x in get_urls(page) if x not in seen]
        for _url in urls:
            await tasks.put(_url)

        for e in get_edges(url, urls):
            await edges.put(e)

        tasks.task_done()
        seen.add(url)


async def write_to_file():
    global nEdges
    while 1:
        line = await edges.get() + "\n"
        await out.write(line)
        edges.task_done()
        nEdges += 1


async def finish_up():
    while nEdges < edgeLimit:
        await asyncio.sleep(1)
    edges.join()
    out.close()
    loop.stop()
    client.close()
    print("elapsed: ", time.time() - start)


async def monitor():
    while 1:
        await asyncio.sleep(15)
        print(f"{len(seen)} have been processed, time elapsed: {time.time() - start:.2f}s")


start = time.time()
asyncio.ensure_future(init())
for i in range(10):  # get us n workers
    asyncio.ensure_future(worker(i))
asyncio.ensure_future(write_to_file())
asyncio.ensure_future(finish_up())
asyncio.ensure_future(monitor())
loop.run_forever()

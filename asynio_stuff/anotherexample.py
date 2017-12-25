import asyncio
import aiohttp
from util.simplejson import loads
import time


class TaskCounter:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __bool__(self):
        return self.n != 0

    def decrement(self):
        self.n -= 1


loop = asyncio.get_event_loop()
client = aiohttp.ClientSession(loop=loop)


async def get_json(client, url):
    async with client.get(url) as response:
        if response.status != 200:
            return
        return await response.read()


async def get_reddit_top(subreddit, client, counter):
    data1 = await get_json(client, 'https://www.reddit.com/r/'+subreddit+ '/top.json?sort=top&t=day&limit=5')
    if data1:
        j = loads(data1.decode("utf-8"))
        print(j)
    counter.decrement()


async def finish_up(counter):
    while counter:
        await asyncio.sleep(0.1)
        print(counter.n)
    await client.close()
    finish = time.time()
    print("elapsed:", finish-start)
    out.close()
    loop.stop()


start = time.time()
topics1 = ["python", "golang", "haskell", "rustlang", "java", "javascript", "coffeescript", "react"]
topics2 = ["python"]
taskCounter = TaskCounter(len(topics1))


for t in topics1:
    asyncio.ensure_future(get_reddit_top(t, client, taskCounter))
asyncio.ensure_future(finish_up(taskCounter))
loop.run_forever()



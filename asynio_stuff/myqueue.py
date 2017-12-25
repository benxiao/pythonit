from collections import deque
from threading import Thread
from concurrent.futures import Future
from threading import Lock
from asyncio import wait_for, wrap_future, get_event_loop, Queue

# resembles queue.Queue
# class MyQueue:
#     def __init__(self, maxsize):
#         self.maxsize = maxsize
#         self.items = deque()
#
#     def get(self):
#         return self.items.popleft()
#
#     def put(self, item):
#         if len(self.items) < self.maxsize:
#             self.items.append(item)
#         else:
#             print("No")
"""
 There are no circumstance where you can have both getters and putters are non-empty
"""


class MyQueue:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.items = deque()
        self.getters = deque()
        self.putters = deque()
        self.mutex = Lock()

    def get_noblock(self):
        if self.items:
            # wake a putter
            if self.putters:
                self.putters.popleft().set_result(True)
            self.putters.popleft().set_result(True)
            return self.items.popleft(), None
        else:
            fut = Future()
            self.getters.append(fut)
            return None, fut

    def put_noblock(self, item):
        """
        When the queue is full, ignore further input
        :param item:
        :return:
        """
        if len(self.items) < self.maxsize:
            self.items.append(item)
            # wake up a getter
            if self.getters:
                self.getters.popleft().set_result(self.items.popleft())
        else:
            fut = Future()
            self.putters.append(fut)
            return fut

    def get_sync(self):
        item, fut = self.get_noblock()
        if fut:
            item = fut.result()
        return item

    async def get_async(self):
        item, fut = self.get_noblock()
        if fut:
            item = await wait_for(wrap_future(fut), None)
        return item

    def put_sync(self, item):
        # don't understand the point of having this while loop
        while 1:
            fut = self.put_noblock(item)
            if not fut:
                return
            fut.result()

    async def put_async(self, item):
        while 1:
            fut = self.put_noblock(item)
            if not fut:
                return
            await wait_for(wrap_future(fut), None)


if __name__ == '__main__':
    pass

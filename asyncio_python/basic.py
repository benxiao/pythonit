from asyncio import get_event_loop


async def helloWorld(x):
    print(f"hello {x}")
    await helloUnderWorld(x)


async def helloUnderWorld(y):
    print(f"hello underworld {y}")


async def greetingToGroup(group):
    [await helloWorld(x) for x in group]





loop = get_event_loop()
loop.run_until_complete(greetingToGroup(["John", "Alex", "Jones"]))

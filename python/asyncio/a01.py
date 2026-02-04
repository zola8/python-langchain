import asyncio


async def func1():
    print("A")
    # await asyncio.sleep(1)
    await func2()
    print("B")

async def func2():
    print("C")
    await asyncio.sleep(2)
    print("D")

asyncio.run(func1())
# A C D B - we wait the 2nd func2()... avoid that we create a task


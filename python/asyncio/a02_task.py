import asyncio


async def func1():
    task = asyncio.create_task(func2())
    print("A")
    await asyncio.sleep(1)
    print("B")
    await task


async def func2():
    print("C")
    await asyncio.sleep(2)
    print("D")


asyncio.run(func1())

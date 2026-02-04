import asyncio


async def func1():
    task = asyncio.create_task(func2())
    print("A")
    await asyncio.sleep(1)
    print("B")

    # promise in JS, future in Java
    return_value = await task
    print("return_value:", return_value)


async def func2():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10


asyncio.run(func1())

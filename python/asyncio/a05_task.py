import asyncio


async def fetch_data(id, delay):
    print(f'{id} Fetching data...')
    await asyncio.sleep(delay)
    print(f'{id} Fetched data!')
    return {'id': id, 'data': 'some data'}


async def main():
    task1 = asyncio.create_task(fetch_data(1, 3))
    task2 = asyncio.create_task(fetch_data(2, 1))
    task3 = asyncio.create_task(fetch_data(3, 2))

    result1 = await task1
    result2 = await task2
    result3 = await task3

    print("received results:", result1, result2, result3)
    print('program end')


if __name__ == '__main__':
    asyncio.run(main())

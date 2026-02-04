import asyncio


async def fetch_data(id, delay):
    print(f'{id} Fetching data...')
    await asyncio.sleep(delay)
    print(f'{id} Fetched data!')
    return {'id': id, 'data': 'some data'}


async def main():
    task1 = fetch_data(1, 2)
    task2 = fetch_data(2, 2)

    result1 = await task1
    print("received result:", result1)
    # coroutine doesnt start running until awaited, we have no benefit yet here

    result2 = await task2
    print("received result:", result2)

    print('program end')


if __name__ == '__main__':
    asyncio.run(main())

import asyncio


async def fetch_data(id, delay):
    print(f'{id} Fetching data...')
    await asyncio.sleep(delay)
    print(f'{id} Fetched data!')
    return {'id': id, 'data': 'some data'}


async def main():
    # instead of task creating, we just pass the coroutine objects
    # gather - not so good when we have an error!
    results = await asyncio.gather(fetch_data(1, 3), fetch_data(2, 1), fetch_data(3, 2))
    print("received results:", results)
    print('program end')


if __name__ == '__main__':
    asyncio.run(main())

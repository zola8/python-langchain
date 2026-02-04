import asyncio


async def fetch_data(id, delay):
    print(f'{id} Fetching data...')
    await asyncio.sleep(delay)
    print(f'{id} Fetched data!')
    return {'id': id, 'data': 'some data'}


async def main():
    tasks = []
    # async with == asyncronous context manager
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]
    print(results)

    print('program end')


if __name__ == '__main__':
    asyncio.run(main())

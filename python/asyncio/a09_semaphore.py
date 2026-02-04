import asyncio


async def access_resource(semaphore, resource_id):
    async with semaphore:
        print('accessing resource:', resource_id)
        await asyncio.sleep(1)
        print('release resource:', resource_id)


async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))


if __name__ == '__main__':
    asyncio.run(main())

# semaphore = allows multiple coroutines to have access to the same object at the same time


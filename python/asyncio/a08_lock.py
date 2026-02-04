import asyncio

shared_resource = 0

lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    # this async context manager checks if the lock is released
    async with lock:
        print('resource before modification:', shared_resource)
        shared_resource += 1
        await asyncio.sleep(1)
        print('resource after modification:', shared_resource)


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


if __name__ == '__main__':
    asyncio.run(main())

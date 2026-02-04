# https://www.youtube.com/watch?v=Qb9s3UiMSTA
import asyncio


async def waiter(event):
    print('waiting on event to be set:', event)
    await event.wait()
    print('event has been set, continue execution', event)


async def setter(event):
    await asyncio.sleep(2)  # simulate work
    event.set()
    print("event has been set: ", event)


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


if __name__ == '__main__':
    asyncio.run(main())

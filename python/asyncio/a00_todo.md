# kell:
- https://www.youtube.com/watch?v=dEZKySL3M9c - Async for loops in Python                                       - OK
- https://www.youtube.com/watch?v=ftmdDlwMwwQ - Intro to async Python | Writing a Web Crawler                   - OK
- https://www.youtube.com/watch?v=Qb9s3UiMSTA - Asyncio in Python - Full Tutorial (Tech with Tim)               - OK
- https://www.youtube.com/watch?v=RIVcqT2OGPA - Asyncio Finally Explained: What the Event Loop Really Does      - OK
- https://www.youtube.com/watch?v=6RbJYN7SoRs - AsyncIO & Asynchronous Programming in Python (neuralnine)       - OK
 
asyncio, threads, processes -> these are the tools
asyncio - you/CPU wait a lot for file handling, etc
threads are suited for tasks that may have to wait but share data, they can run parallel
processes - maximize performance on CPU intensive tasks

async != not multi-threading, not multi-processing
async == concurrent programming,

when func1() waiting for DB, we use the CPU time to start executing func2()

-------------

# asyncio

event loop = the core that manages and distribute to run task (waiting for tasks and execute them)
co-routines = asyncio.run() -- this start the event loop
    async def func(): ...
    func() == this returns the coroutine object

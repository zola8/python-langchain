import hashlib

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from starlette.routing import Route


# https://www.youtube.com/watch?v=dEZKySL3M9c


async def online_sha256(stream) -> bytes:
    hasher = hashlib.sha256()
    async for chunk in stream:
        print(f"got chunk: {chunk}")
        hasher.update(chunk)
    return hasher.digest()


async def compute_sha256(request: Request):
    bytes_hash = await online_sha256(request.stream())
    return PlainTextResponse(bytes_hash)


routes = [
    Route(path='/', methods=['POST'], endpoint=compute_sha256),
]

app = Starlette(routes=routes, debug=True)


def main():
    import uvicorn
    uvicorn.run(app, port=8080, log_level="info")


if __name__ == '__main__':
    main()

# https://github.com/Niklas-dev/fastapi-lifespan-tutorial/blob/main/examples/02_database_lifespan.py
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

import asyncio


# Simulated database class
class Database:
    def __init__(self):
        self.connected = False
        self.query_count = 0

    async def connect(self):
        """Simulate async database connection."""
        print("  Connecting to database...")
        await asyncio.sleep(0.5)  # Simulate connection time
        self.connected = True
        print("  Database connected!")

    async def disconnect(self):
        """Simulate async database disconnection."""
        print("  Disconnecting from database...")
        await asyncio.sleep(0.2)
        self.connected = False
        print(f"  Database disconnected! (Handled {self.query_count} queries)")

    async def query(self, sql: str):
        """Simulate database query."""
        if not self.connected:
            raise Exception("Database not connected!")
        self.query_count += 1
        return {"result": f"Query executed: {sql}", "query_number": self.query_count}


# Global database instance
db = Database()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan with async database operations.

    Important: Both connect() and disconnect() are async!
    """
    # STARTUP - Connect to database
    print("\nApplication Startup")
    await db.connect()

    yield

    # SHUTDOWN - Disconnect from database
    print("\nApplication Shutdown")
    await db.disconnect()


app = FastAPI(title="Database Lifespan Example", lifespan=lifespan)


@app.get("/")
async def root():
    return {
        "message": "Database connection is managed by lifespan",
        "database_connected": db.connected
    }


@app.get("/query")
async def execute_query(sql: str = "SELECT * FROM users"):
    """Execute a database query."""
    result = await db.query(sql)
    return result


@app.get("/stats")
async def get_stats():
    """Get database stats."""
    return {
        "connected": db.connected,
        "total_queries": db.query_count
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

import asyncio
from pymongo import AsyncMongoClient

async def main():
    uri = "mongodb+srv://23315a0522_db_user:Admin123@cluster0.ede4xu4.mongodb.net/"
    client = AsyncMongoClient(uri)

    await client.admin.command("ping")
    print("Connected successfully")
    await client.close()

asyncio.run(main())
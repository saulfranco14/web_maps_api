import motor.motor_asyncio
import os
from decouple import config

async def Database(table: str) -> motor.motor_asyncio.AsyncIOMotorCollection:
    MONGO_DETAILS = config("MONGODB_URL")
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
    database = client.web_maps
    return database.get_collection(table)

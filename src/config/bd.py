import  motor.motor_asyncio
import  os
from    decouple            import config

MONGO_DETAILS       = config("MONGODB_URL")
client              = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database            = client.web_maps

async def Database(table):
    data_collection   = database.get_collection(table)
    return data_collection

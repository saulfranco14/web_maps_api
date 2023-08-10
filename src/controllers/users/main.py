from src.config.bd import Database
from bson.objectid import ObjectId

# Connect to Mongo
user_collection = Database("User")

def user_helper(user) -> dict:
    
    # Return a simplified dictionary
    return {
        "id_user": str(user["_id"]),
        "name_user": str(user["name_user"]),
        "gender_user": str(user["gender_user"]),
        "municipality_user": str(user["municipality_user"]),
        "state_user": str(user["state_user"]),
    }

async def all_users():
    users = [user_helper(user) async for user in user_collection.find()]
    return users

async def add_user(user_data: dict) -> dict:
    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})
    return user_helper(new_user)

async def id_user(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

async def get_user_by_id(id: str) -> dict:
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        return user_helper(user)

async def update_user(id: str, data: dict):
    if len(data) < 1:
        return False
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        updated_user = await user_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return bool(updated_user)

async def delete_user(id: str):
    user = await user_collection.find_one({"_id": ObjectId(id)})
    if user:
        await user_collection.delete_one({"_id": ObjectId(id)})
        return True

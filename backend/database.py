from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DETAILS = "mongodb://localhost:27017"  # Remplacer par ton MongoDB Atlas si besoin
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["dating_app"]

users_collection = database.get_collection("users")
locations_collection = database.get_collection("locations")
likes_collection = database.get_collection("likes")
matches_collection = database.get_collection("matches")
crossings_collection = database.get_collection("crossings")
tokens_collection = database.get_collection("tokens")
messages_collection = database.get_collection("messages")


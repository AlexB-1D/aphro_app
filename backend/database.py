# backend/database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os

# URL MongoDB
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://dev:aphro_dev@test.yo2zogh.mongodb.net/?retryWrites=true&w=majority&appName=test"
)

# Création du client MongoDB asynchrone
client = AsyncIOMotorClient(MONGO_URL)

# Sélection de la base de données
db = client["aphro_db"]

# Collections
users_collection = db["users"]
likes_collection = db["likes"]
tokens_collection = db["tokens"]
messages_collection = db["messages"]
device_tokens_collection = db["device_tokens"]

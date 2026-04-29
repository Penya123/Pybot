from pymongo import MongoClient
from datetime import datetime

MONGO_HOST="localhost"
MONGO_PORT="27017"

MONGO_URL="mongodb://" + MONGO_HOST + ":" + MONGO_PORT + "/"

client = MongoClient(MONGO_URL)
db = client["pychat"]
chats = db["chats"]

def save_message(sender, message, number):
    chats.insert_one(
        {
            "remitente": sender,
            "numero": number,
            "mensaje": message,
            "datetime": str(datetime.now())
        }
    )

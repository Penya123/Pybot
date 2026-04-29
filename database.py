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

def get_last_messages(limit = 3):
    return list(reversed(list(chats.find().sort("numero", -1).limit(limit)))) 

def get_next_number():
    last = chats.find_one(sort=[("numero", - 1)])
    return (last["numero"] + 1) if last else 0
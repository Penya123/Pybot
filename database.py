import pymongo

MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_TIMEOUT=1000

MONGO_URL="mongodb://" + MONGO_HOST + ":" + MONGO_PORT + "/"

databaseName = "pychat"
dbCollection = "chats"

try:
    cliente=pymongo.MongoClient(MONGO_URL, serverSelectionTimeoutMS=MONGO_TIMEOUT)
    cliente.server_info()
    print("Succesfull connection")

    database = cliente[databaseName]
    collection = database[dbCollection]

    for documents in collection.find():
        print("Remitente: " + documents["remitente"] +
              "\nMensaje: " + documents["mensaje"] + 
              "\nHora: " + documents["datetime"])

    cliente.close
except pymongo.errors.ServerSelectionTimeoutError as Timefail:
    print("Time out: " + Timefail)
except pymongo.errors.ConnectionFailure as errorConnection:
    print("fail to connecto to MongoDB: " + errorConnection)
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(".env")

MONGO_DB= os.environ.get("MONGO_DB_URI")
# print(MONGO_DB)

#db_client = MongoClient("mongodb+srv://fullstack:letras@cluster0.vq2db.mongodb.net/?retryWrites=true&w=majority").test
db_client = MongoClient().local
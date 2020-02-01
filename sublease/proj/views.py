from pymongo import MongoClient

from pprint import pprint

client = MongoClient("mongodb+srv://guest:root@listings-gru4r.mongodb.net/test?retryWrites=true&w=majority")

db = client.admin

serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)

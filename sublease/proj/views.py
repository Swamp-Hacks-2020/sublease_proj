from pymongo import MongoClient

from pprint import pprint

client = MongoClient("mongodb+srv://guest:root@listings-gru4r.mongodb.net/test?retryWrites=true&w=majority")

db = client.business

#serverStatusResult = db.command("serverStatus")
#pprint(serverStatusResult)

testListing = {

	'listing_id' : "00000001",
	'apartment_name' : "Gainesville Place",
	'num_bedrooms' : 4,
	
	'lister_name' : "MingYEEN" 

}

result = db.listings.insert_one(testListing)


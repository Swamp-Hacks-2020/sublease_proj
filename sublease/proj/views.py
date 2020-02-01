from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

from pprint import pprint

client = MongoClient("mongodb+srv://guest:root@listings-gru4r.mongodb.net/test?retryWrites=true&w=majority")
db = client.business

#serverStatusResult = db.command("serverStatus")
#pprint(serverStatusResult)
def listings(request):
    testListing = {

	   'listing_id' : "00000001",
	   'apartment_name' : "Gainesville Place",
	   'num_bedrooms' : 4,
	   'lister_name' : "MingYEEN"
       }

    #result = db.listings.insert_one(testListing)
    return render(request, "listing.html")

def home(request):
    return render(request, "home.html")

def view(request):
	all_listings = db.listings.find({}) #by default, present all listings
	
	args = { 'all' : all_listings}
	
	return render(request, "view.html", args)

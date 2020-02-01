from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from .forms import*
from pprint import pprint

client = MongoClient("mongodb+srv://guest:root@listings-gru4r.mongodb.net/test?retryWrites=true&w=majority")
db = client.business

#serverStatusResult = db.command("serverStatus")
#pprint(serverStatusResult)
def listings(request):

	form_user = getUserInfo(request.POST or None)
	form_apt = getApartmentInfo(request.POST or None)

	if form_user.is_valid():
		name = form_user.cleaned_data['name']
		phone = form_user.cleaned_data['phone']
		email = form_user.cleaned_data['email']
	else:
		name = ""
		phone = ""
		email = ""

	if form_apt.is_valid():
		street1 = form_user.cleaned_data['street1']
		street2 = form_user.cleaned_data['street2']
		city = form_user.cleaned_data['city']
		zip = form_user.cleaned_data['zip']
		semester = form_user.cleaned_data['semester']
		complex = form_user.cleaned_data['complex']
		bedrooms = form_user.cleaned_data['bedrooms']
		bathrooms = form_user.cleaned_data['bathrooms']
		cost = form_user.cleaned_data['cost']
		utilities = form_user.cleaned_data['utilities']
	else:
		street1 = ""
		street2 = ""
		city = ""
		zip = ""
		semester = ""
		complex = ""
		bedrooms = ""
		bathrooms = ""
		cost = ""
		utilities = ""

	listing = {

	}

	args = {'form_user' : form_user, 'form_apt': form_apt}
	return render(request, "listing.html", args)

def home(request):
    return render(request, "home.html")

def directory(request):
	all_listings = db.listings.find({}) #by default, present all listings

	args = { 'all' : all_listings}

	return render(request, "directory.html", args)

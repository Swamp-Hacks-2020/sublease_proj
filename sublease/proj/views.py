from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from pymongo import MongoClient
from .forms import*
from pprint import pprint
import smtplib, ssl
from bson.objectid import ObjectId


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
		street1 = form_apt.cleaned_data['street1']
		street2 = form_apt.cleaned_data['street2']
		city = form_apt.cleaned_data['city']
		zip = form_apt.cleaned_data['zip']
		semester = form_apt.cleaned_data['semester']
		complex = form_apt.cleaned_data['complex']
		bedrooms = form_apt.cleaned_data['bedrooms']
		bathrooms = form_apt.cleaned_data['bathrooms']
		cost = form_apt.cleaned_data['cost']
		utilities = form_apt.cleaned_data['utilities']
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
		'Leaser Name' : name,
		'Phone' : phone,
		'Email' : email,
		'Address 1' : street1,
		'Address 2' : street2,
		'City' : city,
		'Zip' : zip,
		'Semester' : semester,
		'Complex' : complex,
		'Bedrooms' : bedrooms,
		'Bathrooms' : bathrooms,
		'Cost' : cost
	}
	if name != "":
		obj = db.listings.insert_one(listing)
		#print(obj.inserted_id)
		context = ssl.create_default_context()
		message = """\
Subject: Sublease ID

Your id is: """ + str(obj.inserted_id)
		emailserv = smtplib.SMTP(host = 'smtp.gmail.com', port = 587) #587 html
		emailserv.starttls(context = context)
		emailserv.login('swampysublease@gmail.com', 'swamphacks2020')
		emailserv.sendmail('swampysublease@gmail.com', email, message)
		emailserv.quit()
		return HttpResponseRedirect(('/listing/success'))
	else:
		args = {'form_user' : form_user, 'form_apt': form_apt}
		return render(request, 'listing.html', args)

def success(request):
	return render(request, "success.html")

def home(request):
    return render(request, "home.html")

def update(request):
	form_user = getUserInfo(request.POST or None)
	form_apt = getApartmentInfo(request.POST or None)

	form_token = getToken(request.POST or None)
	if form_token.is_valid():
		token = form_token.cleaned_data['token']
	else:
		token = ""
	if token != "":
		result = db.listings.delete_many({"_id": ObjectId(token)})
		return HttpResponseRedirect(('/update/deleted'))
	args = {'form_token' : form_token}
	return render(request, "update.html", args)

def deleted(request):
	return render(request, "deleted.html")

def directory(request):
	form_filter = filterApartmentListings(request.POST or None)
	if form_filter.is_valid():
		bedrooms = form_filter.cleaned_data('bedrooms')
		bathrooms = form_filter.cleaned_data('bathrooms')
		priceRange = form_filter.cleaned_data('priceRange')
		complexName = form_filter.cleaned_data('complexName')
	all_listings = db.listings.find({}) #by default, present all listings
	all_data = []
	headers = list(all_listings[0].keys())[1:]
	for listing in all_listings:
		all_data.append(list(listing.values())[1:])
	args = { 'all' : all_data, 'headings': headers, 'form_filter': form_filter}

	return render(request, "directory.html", args)

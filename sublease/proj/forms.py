from django import forms
from django_range_slider.fields import RangeSliderField
from django.forms.widgets import NumberInput, RadioSelect

class RangeInput(NumberInput):
    input_type = 'range'

CHOICES = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5+')]

class getUserInfo(forms.Form):
    name = forms.CharField(label = 'Name', widget = forms.TextInput(attrs = {'placeholder' : 'Name'}), max_length = 50)
    phone = forms.CharField(label = 'Phone Number', widget = forms.TextInput(attrs = {'placeholder' : '(000)-000-0000'}), max_length = 14)
    email = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder' : 'email@example.com'}), max_length = 200)

class getApartmentInfo(forms.Form):
    street1 = forms.CharField(label = 'Street 1', widget = forms.TextInput(attrs = {'placeholder' : 'Street Address'}))
    street2 = forms.CharField(label = 'Street 2', widget = forms.TextInput(attrs = {'placeholder' : 'Apt, Bldg, Suite, etc.'}), required = False)
    city = forms.CharField(label = 'City', widget = forms.TextInput(attrs = {'placeholder' : 'City'}))
    zip = forms.CharField(label = 'Zip', widget = forms.TextInput(attrs = {'placeholder' : 'Zip (00000)'}), max_length = 5)
    semester = forms.CharField(label = 'Semester', widget = forms.TextInput(attrs = {'placeholder' : 'Semester Availabile (i.e. Fall 2020, Spring 2020, Summer 2020)'}), max_length = 15)
    complex = forms.CharField(label = 'Complex', widget = forms.TextInput(attrs = {'placeholder' : 'Apartment Complex'}))
    bedrooms = forms.CharField(label = 'Bedrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bedrooms'}), max_length = 1)
    bathrooms = forms.CharField(label = 'Bathrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bathrooms'}), max_length = 1)
    cost = forms.CharField(label = 'Cost', widget = forms.TextInput(attrs = {'placeholder' : 'Cost per Month'}))
    utilities = forms.CharField(label = 'Utilities', widget = forms.TextInput(attrs = {'placeholder' : 'Utilities Included (i.e. Yes, No)'}))

class filterApartmentListings(forms.Form):
    #checkbox form with options for floorplans
    #bedrooms = forms.MultipleChoiceField(choices = CHOICES, widget = forms.CheckboxSelectMultiple())
    #bathrooms = forms.MultipleChoiceField(choices = CHOICES, widget = forms.CheckboxSelectMultiple())
    #slider form for price ranges (maybe just checkboxes with built in ranges)
    maxPrice = forms.IntegerField(widget = forms.TextInput(attrs = {'placeholder' : 'Maximum Price'}), required = False)
    #search based on complex name
    complexName = forms.CharField(label = 'Complex Name', widget = forms.TextInput(attrs = {'placeholder' : 'Complex Name'}), required = False)

    #going to use this inside of the directory views, and then instead of find all from the database, use the form input to narrow down the results
    #can be autorefresh or submit form first and then get results, one significantly harder than the other
class getToken(forms.Form):
    token = forms.CharField(label = 'Token', widget = forms.TextInput(attrs = {'placeholder' : 'Token Val'}), max_length = 24)

from django import forms
import phonenumbers


class getUserInfo(forms.Form):
    name = form.CharField(label = 'Name', widget = forms.TextInput(attrs = {'placeholder' = 'Name'}, max_length = 50))
    phone1 = form.CharField(label = 'Area code', widget = forms.TextInput(attrs = {'placeholder' = '123'}, max_length = 3, min_length = 3))
    phone2 = form.CharField(label = 'Number', widget = forms.TextInput(attrs = {'placeholder' = '456'}, max_length = 3, min_length = 3))
    phone3 = form.CharField(label = 'Number', widget = forms.TextInput(attrs = {'placeholder' = '7890'}, max_length = 4, min_length = 4))

class getApartmentInfo(forms.Form):
    address = form.CharField(label = 'Address', widget = forms.TextInput(attrs = {'placeholder' = 'Apartment Address'}))
    #Caleb updates
    complex = form.CharField(label = 'Complex', widget = forms.TextInput(attrs = {'placeholder' = 'Apartment Complex (Optional)'}, required = false))
    bedrooms = form.CharField(label = 'Bedrooms', widget = forms.TextInput(attrs = {'placeholder' = 'Number of Bedrooms'}, max_length = 1))
    bathrooms = form.CharField(label = 'Bathrooms', widget = forms.TextInput(attrs = {'placeholder' = 'Number of Bathrooms', max_length = 1}))
    cost = form.CharField(label = 'Cost', widget = forms.TextInput(attrs = {'placeholder' = 'Cost per Month'}))
    utilities = form.BooleanField(label = 'Utilities', widget = )

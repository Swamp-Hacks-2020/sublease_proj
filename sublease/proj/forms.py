from django import forms

class getUserInfo(forms.Form):
    name = form.CharField(label = 'Name', widget = forms.TextInput(attrs = {'placeholder' = 'Name'}, max_length = 50))
    phone = form.CharField(label = 'Phone', widget = forms.TextInput(attrs = {'placeholder' = 'Phone Number'}, max_length = 12))
    #add in validation

class getApartmentInfo(forms.Form):
    address = form.CharField(label = 'Address', widget = forms.TextInput(attrs = {'placeholder' = 'Apartment Address'}))
    #add in formatting
    complex = form.CharField(label = 'Complex', widget = forms.TextInput(attrs = {'placeholder' = 'Apartment Complex (Optional)'}, required = false))
    bedrooms = form.CharField(label = 'Complex', widget = )

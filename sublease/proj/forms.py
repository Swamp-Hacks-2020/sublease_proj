from django import forms


class getUserInfo(forms.Form):
    name = forms.CharField(label = 'Name', widget = forms.TextInput(attrs = {'placeholder' : 'Name'}), max_length = 50)
    phone = forms.CharField(label = 'Phone Number', widget = forms.TextInput(attrs = {'placeholder' : '(000)-000-0000'}), max_length = 14)
    email = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder' : 'email@example.com'}), max_length = 200)

class getApartmentInfo(forms.Form):
    street1 = forms.CharField(label = 'Street 1', widget = forms.TextInput(attrs = {'placeholder' : 'Street Address'}))
    street2 = forms.CharField(label = 'Street 2', widget = forms.TextInput(attrs = {'placeholder' : 'Apt, Bldg, Suite, etc.'}), required = False)
    city = forms.CharField(label = 'City', widget = forms.TextInput(attrs = {'placeholder' : 'Metropolis'}))
    zip = forms.CharField(label = 'Zip', widget = forms.TextInput(attrs = {'placeholder' : '00000'}), max_length = 5)
    semester = forms.CharField(label = 'Semester', widget = forms.TextInput(attrs = {'placeholder' : 'Semester Availabile (i.e. Fall 2020, Spring 2020, Summer 2020)'}), max_length = 15)
    complex = forms.CharField(label = 'Complex', widget = forms.TextInput(attrs = {'placeholder' : 'Apartment Complex'}))
    bedrooms = forms.CharField(label = 'Bedrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bedrooms'}), max_length = 1)
    bathrooms = forms.CharField(label = 'Bathrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bathrooms'}), max_length = 1)
    cost = forms.CharField(label = 'Cost', widget = forms.TextInput(attrs = {'placeholder' : 'Cost per Month'}))
    utilities = forms.ChoiceField(choices = [("Included", "Included"), ("Not Included", "Not included")]) #need to check syntax

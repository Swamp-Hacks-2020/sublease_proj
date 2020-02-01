from django import forms


UTILITIES_CHOICES = [
 ('Included', 'Included'),
 ('Not Included', 'Not Included'),
]

class getUserInfo(forms.Form):
    name = forms.CharField(label = 'Name', widget = forms.TextInput(attrs = {'placeholder' : 'Name'}), max_length = 50)
    phone = forms.CharField(label = 'Phone Number', widget = forms.TextInput(attrs = {'placeholder' : '(000)-000-0000'}), max_length = 14)
    email = forms.EmailField(widget = forms.TextInput(attrs = {'placeholder' : 'email@example.com'}), max_length = 200)

class getApartmentInfo(forms.Form):
    street1 = forms.CharField(label = 'Street 1', widget = forms.TextInput(attrs = {'placeholder' : 'Street Address'}))
    street2 = forms.CharField(label = 'Street 2', widget = forms.TextInput(attrs = {'placeholder' : 'Apt, Bldg, Suite, etc.'}), required = False)
    city = forms.CharField(label = 'City', widget = forms.TextInput(attrs = {'placeholder' : 'Metropolis'}))
    zip = forms.CharField(label = 'Zip', widget = forms.TextInput(attrs = {'placeholder' : 'Zip (00000)'}), max_length = 5)
    semester = forms.CharField(label = 'Semester', widget = forms.TextInput(attrs = {'placeholder' : 'Semester Availabile (i.e. Fall 2020, Spring 2020, Summer 2020)'}), max_length = 15)
    complex = forms.CharField(label = 'Complex', widget = forms.TextInput(attrs = {'placeholder' : 'Apartment Complex'}))
    bedrooms = forms.CharField(label = 'Bedrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bedrooms'}), max_length = 1)
    bathrooms = forms.CharField(label = 'Bathrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bathrooms'}), max_length = 1)
    cost = forms.CharField(label = 'Cost', widget = forms.TextInput(attrs = {'placeholder' : 'Cost per Month'}))
    utilities = forms.CharField(label = 'Utilities', widget = forms.TextInput(attrs = {'placeholder' : 'Utilities Included (i.e. Yes, No)'}))

class filterApartmentListings(forms.Form):
    a=5
    #checkbox form with options for floorplans
    #slider form for price ranges (maybe just checkboxes with built in ranges)
    #search based on complex name
    #going to use this inside of the directory views, and then instead of find all from the database, use the form input to narrow down the results
    #can be autorefresh or submit form first and then get results, one significantly harder than the other

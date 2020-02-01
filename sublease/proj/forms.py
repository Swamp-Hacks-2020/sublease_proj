from django import forms


class getUserInfo(forms.Form):
    name = forms.CharField(label = 'Name', widget = forms.TextInput(attrs = {'placeholder' : 'Name'}), max_length = 50)
    phone1 = forms.CharField(label = 'Area code', widget = forms.TextInput(attrs = {'placeholder' : '123'}), max_length = 3)
    phone2 = forms.CharField(label = 'Number', widget = forms.TextInput(attrs = {'placeholder' : '456'}), max_length = 3)
    phone3 = forms.CharField(label = 'Number', widget = forms.TextInput(attrs = {'placeholder' : '7890'}), max_length = 4)
    email = forms.EmailField(max_length = 200)

class getApartmentInfo(forms.Form):
    street1 = forms.CharField(label = 'Street 1', widget = forms.TextInput(attrs = {'placeholder' : ''}))
    street2 = forms.CharField(label = 'Street 2', widget = forms.TextInput(attrs = {'placeholder' : ''}))
    city = forms.CharField(label = 'City', widget = forms.TextInput(attrs = {'placeholder' : ''}))
    zip = forms.CharField(label = 'Street 2', widget = forms.TextInput(attrs = {'placeholder' : ''}), max_length = 5)
    semester = forms.CharField(label = 'Semester', widget = forms.TextInput(attrs = {'placeholder' : 'ex: Fall 2020, Spring 2020, Summer 2020'}), max_length = 15)
    complex = forms.CharField(label = 'Complex', widget = forms.TextInput(attrs = {'placeholder' : 'Apartment Complex (Optional)'}), required = False)
    bedrooms = forms.CharField(label = 'Bedrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bedrooms'}), max_length = 1)
    bathrooms = forms.CharField(label = 'Bathrooms', widget = forms.TextInput(attrs = {'placeholder' : 'Number of Bathrooms'}), max_length = 1)
    cost = forms.CharField(label = 'Cost', widget = forms.TextInput(attrs = {'placeholder' : 'Cost per Month'}))
    utilities = forms.ChoiceField(choices = ("Included", "Not included")) #need to check syntax

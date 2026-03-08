from django import forms

class userRegistration(forms.Form):
    # Creating User Registration form
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    
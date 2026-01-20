from django import forms

class userRegistration(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    
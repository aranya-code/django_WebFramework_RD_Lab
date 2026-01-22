from django import forms
from movieList.models import movie

class movieCreation(forms.ModelForm):
    class Meta:
        model = movie
        fields = '__all__'
        


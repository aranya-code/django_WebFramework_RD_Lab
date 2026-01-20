from django.shortcuts import render
from . import forms


def UserRegistrationView(request):
    form = forms.userRegistration()
    if form.is_valid():
        if request.method == 'POST':
            forms.userRegistration(request.POST)
    else:
        forms.userRegistration()
    return render (request,'formsApp/userform.html',{'form':form})
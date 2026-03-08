from django.shortcuts import render
from . import forms


# View function to handle user registration form
def UserRegistrationView(request):

    # Create an empty form instance when the page loads (GET request)
    form = forms.userRegistration()

    # Check if the form is submitted using POST request
    if request.method == 'POST':

        # Bind the submitted data to the form
        form = forms.userRegistration(request.POST)

        # Validate the form data
        if form.is_valid():

            # If the form is valid, cleaned_data contains validated input
            print('Success', form.cleaned_data)

    # Render the template and pass the form to the HTML page
    return render(request, 'formsApp/userform.html', {'form': form})
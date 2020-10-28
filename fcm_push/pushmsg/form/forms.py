from django import forms


# creating a form
class InputForm(forms.Form):
    title = forms.CharField(max_length=200)
    message = forms.CharField(max_length=200)
    registration_token = forms.CharField(max_length=200)

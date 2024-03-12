from django.forms import Form
from django import forms

class SubscriberForm(Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email = forms.EmailField()
from django.db import models
from django import forms


class ContactForm(forms.Form):
    yourname = forms.CharField(max_length=100, label='Your name')
    email = forms.EmailField(required=False, label='Your email address')
    phone = forms.IntegerField(label='Your contact number')
    catname = forms.CharField(max_length=50, label='Your cat\'s name')
    message = forms.CharField(widget=forms.Textarea, label='Tell us a little bit about your cat, which service you are interested in, and which dates, if you know.')


# Create your models here.
# class Customer(models.Model)


# class Treatment(models.Model)


# class Reservation(models.Model)
from django import forms
from django.forms import ModelForm
from .models import PostImage



class SubscriberForm(forms.Form):
    email = forms.EmailField(label='',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': '', 'placeholder':'Email'}))

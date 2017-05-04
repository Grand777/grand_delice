from django import forms
from .models import *


class SubscriberForm(forms.ModelForm):
    model = Subscriber
    exclude = ['']
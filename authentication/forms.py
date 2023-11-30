from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from store.models import Customer

class CustomerRegistrationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = '__all__'
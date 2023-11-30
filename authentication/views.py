from django.shortcuts import render

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomerRegistrationForm


class CustomerLoginView(LoginView):
    template_name = 'authentication/customer_login.html'
    def get_success_url(self):
        return reverse_lazy('store')

class CustomerRegistrationView(CreateView):
    template_name = 'authentication/customer_registration.html'
    form_class = CustomerRegistrationForm
    def get_success_url(self):
        return reverse_lazy('login')
    
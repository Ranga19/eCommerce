from django.urls import path
from .views import CustomerLoginView, CustomerRegistrationView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomerLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', CustomerRegistrationView.as_view(), name='register'),
]
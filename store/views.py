from django.shortcuts import render

# Create your views here.
from .models import Product

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context=context)

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')
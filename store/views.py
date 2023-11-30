from django.shortcuts import render

# Create your views here.
from .models import Product, Customer, Order, OrderItem

def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context=context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context=context)


def checkout(request):
    return render(request, 'store/checkout.html')
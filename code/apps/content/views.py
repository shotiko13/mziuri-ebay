from django.shortcuts import render, redirect
from .models import Product, Cart
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.core.exceptions import ValidationError

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

@login_required
def add_to_cart(request, product_id):
    
    product = Product.objects.filter(id=product_id).first()

    cart, created = Cart.objects.get_or_create(
        customer=request.user
    )

    try:
        cart.add_to_cart(product)
        messages.success("დაემატა")
    except ValidationError as e:
        messages.error(e.__str__)
    
    return render("product_list")

@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(customer=request.user)
    return render(request, "cart.html", {"cart": cart})


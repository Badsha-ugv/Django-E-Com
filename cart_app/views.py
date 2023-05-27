from django.shortcuts import render,redirect
from store.models import Product
from .models import Cart,CartItem

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key 
    if not cart:
        cart = request.session.create()
    return cart 

def cart_add(request,product_id):
    product = Product.objects.get(id=product_id)

    # Add existing cart
    try:
        cart = Cart.objects.get(cart_id= _cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id= _cart_id(request))
        cart.save()
    
    # Add product to cart
    try:
        cart_item = CartItem.objects.get(product = product, cart=cart) 
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product = product, cart=cart, quantity=1) 
        cart_item.save()
    
    return redirect('store:cart')

def cart(request):
    context = {

    }
    return render(request, 'store/cart.html', context)
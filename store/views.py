from django.shortcuts import render,get_object_or_404
from .models import Product 
from category.models import Category
from cart_app.views import _cart_id
from cart_app.models import CartItem
from django.http import HttpResponse 
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def store(request,category_slug=None):
    category = None 
    product_list = None 
    if category_slug != None:
        category = get_object_or_404(Category,slug=category_slug)
        product_list = Product.objects.filter(category=category,is_available=True)
        paginator = Paginator(product_list,2) 
        page = request.GET.get('page')
        product_list = paginator.get_page(page)

    else:
        product_list = Product.objects.all().filter(is_available=True).order_by('-created_at')
        paginator = Paginator(product_list,3) 
        page = request.GET.get('page')
        product_list = paginator.get_page(page)
    
    context = {
        'product_list': product_list
    }
    return render(request,'store/store.html',context)


def product_details(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug,slug=product_slug) 
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request),product=product).exists() 
        
    except:
        pass 

    context = {
        'product': product,
        'in_cart': in_cart,

    }
    return render(request,'store/product_details.html',context)
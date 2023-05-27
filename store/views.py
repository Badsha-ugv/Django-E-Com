from django.shortcuts import render,get_object_or_404
from .models import Product 
from category.models import Category


# Create your views here.
def store(request,category_slug=None):
    category = None 
    product_list = None 
    if category_slug != None:
        category = get_object_or_404(Category,slug=category_slug)
        product_list = Product.objects.filter(category=category,is_available=True)
    else:
        product_list = Product.objects.all().filter(is_available=True).order_by('-created_at')
    
    context = {
        'product_list': product_list
    }
    return render(request,'store/store.html',context)


def product_details(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug,slug=product_slug) 
    except:
        pass 

    context = {
        'product': product,
        
    }
    return render(request,'store/product_details.html',context)
from django.shortcuts import render 
from store.models import Product 


def home(request):
    product_list = Product.objects.all().filter(is_available=True).order_by('-created_at')

    context = {
        'products': product_list
    }
    return render(request, 'home.html',context)  

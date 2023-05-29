from .models import CartItem,Cart
from .views import _cart_id

def counter(request):
    item_count = 0
    try:
        cart = Cart.objects.filter(cart_id = _cart_id(request))
        cart_item = CartItem.objects.all().filter(cart=cart[:1])
        for item in cart_item:
            item_count += item.quantity 
    except:
        item_count = 0 
    return dict(item_count=item_count)

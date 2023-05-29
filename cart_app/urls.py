from django.urls import path
from . import views 

urlpatterns = [
    path('',views.cart,name='cart'),
    path('add_cart/<str:product_id>/', views.add_cart, name='add_cart'),

    path('decrement_item/<str:product_id>/', views.decrement_item,name='decrement_item'),
    path('remove_cart_item/<str:product_id>/', views.remove_cart_item,name='remove_cart_item'),


]
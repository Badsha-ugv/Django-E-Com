from django.contrib import admin
from .models import Product 


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','category','stock','is_available') 
    prepopulated_fields = {'slug':('name',)}
    search_fields = ('name','category') 
    list_filter = ('is_available','category')


admin.site.register(Product, ProductAdmin)
from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True) 
    desc = models.TextField(blank=True) 
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='images/product',blank=True) 
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('product_details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.name
    
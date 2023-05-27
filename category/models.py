from django.db import models
from django.urls import reverse 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True )
    slug = models.SlugField(max_length=150,unique=True  )
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/category',blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
            # ordering = ('created',)
            verbose_name = 'Category'
            verbose_name_plural = 'Categories'

    def get_url(self):
         return reverse('filter_by_category',args=[self.slug])
    
    def __str__(self):
        return self.name
    
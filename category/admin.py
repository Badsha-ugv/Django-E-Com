from django.contrib import admin

#import models
from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name','slug') 

#register models here
admin.site.register(Category,CategoryAdmin) 
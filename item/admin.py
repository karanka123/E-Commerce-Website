from django.contrib import admin

# Register your models here.
from .models import Category

from .models import Item

admin.site.register(Category)
admin.site.register(Item)
from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Order_products)
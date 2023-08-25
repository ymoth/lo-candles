from django.contrib import admin

from products.models import Product

# Register your models here.
admin.site.register(Product)

admin.site.site_title = 'LO-Candle | Администрирование'
admin.site.site_header = 'LO-Candle | Администрирование'

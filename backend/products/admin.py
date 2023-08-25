from django.contrib import admin

from products.models import Product

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Create a user admin page
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'is_top')
    # list_filter = ('is_top',)

    # fieldsets = (
    #     (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
    #     ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active')}),
    # )
    #
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )
    #
    # search_fields = ('email',)
    # ordering = ('email',)
    # filter_horizontal = ()


admin.site.register(Product, ProductAdmin)


admin.site.site_title = 'LO-Candle | Администрирование'
admin.site.site_header = 'LO-Candle | Администрирование'

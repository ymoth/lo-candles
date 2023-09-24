from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from orders.models import Order
from users.models import User


class OrderListFilter(admin.SimpleListFilter):
    title = 'Фильтрация по статусу'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        ...


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'status', 'get_contact_data', 'get_phone_number',
        'get_description', 'get_products', 'get_method_delivery',
        'id'
    )

    search_fields = (
        'id',
    )
    search_help_text = 'Поиск по номеру заказа.'
    empty_value_display = 'Пустое место'

    list_max_show_all = 500
    list_filter = ('status', 'user')  # (OrderListFilter,)
    list_editable = ('status',)

    def get_contact_data(self, order: Order) -> str:
        """
        REBASE A CONTACT DATA
        """
        return f'{order.contact_data["first_name"]} {order.contact_data["last_name"]}'

    def get_phone_number(self, order: Order) -> str:
        """
        REBASE A PHONE NUMBER
        """
        return f'{order.contact_data["phone_number"]}'

    def get_description(self, order: Order):
        """
        REBASE A ORDER DESCRIPTION
        """
        return order.contact_data.get('commentary') or 'Не указано'

    def get_products(self, order: Order):
        data = ''
        price = 0

        products = order.get_products()
        for index, product in enumerate(products, 1):
            data += f"\n{index}. {product.product.title} {product.product.price:,}тг ({product.count:,})шт"
            price += product.product.price * product.count

        data += f"\nИтого: {price:,}тг"
        return data

    def get_method_delivery(self, order: Order):
        return order.contact_data.get('delivery') or 'Самовывоз'

    get_contact_data.short_description = 'Контакты'
    get_phone_number.short_description = 'Номер телефона'
    get_description.short_description = 'Комментарий к заказу'
    get_products.short_description = 'Товары'
    get_method_delivery.short_description = 'Метод доставки'

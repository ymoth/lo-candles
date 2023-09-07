from django.urls import path

from products.views import ReturnTopProducts, GetProductsBase

urlpatterns = [
    path('baseList', GetProductsBase.as_view({"get": "retrieve"}), name='base_list_products')
]

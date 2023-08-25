from django.urls import path

from products.views import ReturnTopProducts

urlpatterns = [
    path('topList', ReturnTopProducts.as_view(), name='top_products')
]
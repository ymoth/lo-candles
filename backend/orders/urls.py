from django.urls import path

from orders.views import GetListOrders, CreateOrder

urlpatterns = [
    path("getList", GetListOrders.as_view(), name="get_user_orders"),
    path("create", CreateOrder.as_view(), name="create_user_order"),
]
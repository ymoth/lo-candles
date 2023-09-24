from django.urls import path
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from products.views import ReturnTopProducts, GetProductsBase


class ThrottlingAPIView(APIView):
    throttle_classes = [UserRateThrottle]

    def get(self, request):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


urlpatterns = [
    path('baseList', GetProductsBase.as_view({"get": "retrieve"}), name='base_list_products'),
]


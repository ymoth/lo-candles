import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from products.models import Product
from products.serializers import ProductListSerializer


class ReturnTopProducts(ListAPIView):
    queryset = Product.objects.filter(is_top=True)
    permission_classes = (AllowAny,)
    serializer_class = ProductListSerializer


# Create your views here.
def photo_image_return(
        request: HttpRequest,
        year: str,
        month: str,
        day: str,
        photo_name: str
):
    print(os.path.abspath(''))

    with open(os.path.abspath('') + f'//photos//{year}//{month}//{day}//{photo_name}', "rb") as current_image:
        return HttpResponse(current_image.read(), content_type='image/jpeg')

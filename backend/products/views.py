import os

from django.http import HttpRequest, HttpResponse

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from rest_framework.response import Response

import tortoise

class ReturnTopProducts(APIView):
    permission_classes = (AllowAny,)

    # serializer_class = ProductListSerializer
    def get(self, request: HttpRequest):
        queryset = Product.objects.filter(is_top=True)
        return Response(
            status=200, data={
                "count": len(queryset),
                "items": [
                    {
                        'title': product.title.encode('utf-8'),
                        'photo': product.photo.url,
                        'price': product.price,
                        'is_top': product.is_top,
                        'id': product.id
                    } for product in queryset
                ]}
        )


# Create your views here.
def photo_image_return(
        request: HttpRequest,
        year: str, month: str,
        day: str, photo_name: str
) -> HttpResponse:
    with open(os.path.abspath('') + f'//photos//{year}//{month}//{day}//{photo_name}', "rb") as current_image:
        return HttpResponse(current_image.read(), content_type='image/jpeg')


class GetProductsBase(ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    serializer_class = None

    def retrieve(self, request, *args, **kwargs):
        return Response(
            {"items": [
                {
                    'title': product.title.encode('utf-8'),
                    'photo': product.photo.url,
                    'price': product.price,
                    'is_top': product.is_top,
                    'id': product.id,
                    'category': product.category
                } for product in self.get_queryset()
            ]}
        )

    def get_queryset(self):
        data = self.request.data
        if data.get('payload'):
            return Product.objects.filter(**data['payload']['filtering'])
        return Product.objects.filter(is_published=True)


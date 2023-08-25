import os.path

from django.http import HttpRequest, HttpResponse
from rest_framework import routers, serializers, viewsets

from products.models import Product


# Serializers define the API representation.
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'title', 'price',
            'id', 'photo'
        )

    def get_photo_url(self, product: Product):
        return product.photo.url


# ViewSets define the view behavior.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related()
    serializer_class = ProductSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)


def photo_image_return(request: HttpRequest, year: str, month: str, day: str, photo_name: str):
    with open(os.path.abspath('') + f'\\photos\\{year}\\{month}\\{day}\\{photo_name}', "rb") as current_image:
        return HttpResponse(current_image.read(), content_type='image/jpeg')

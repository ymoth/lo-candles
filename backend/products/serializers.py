from rest_framework.serializers import ModelSerializer

from products.models import Product


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'title',
            'price',
            'photo',
            'id',
            'string_price'
        )




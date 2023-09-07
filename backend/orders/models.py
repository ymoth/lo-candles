import dataclasses
import typing

from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import QuerySet

from products.models import Product
from django.utils.translation import gettext_lazy


@dataclasses.dataclass
class _ProductModel:
    product: Product
    count: int

    def as_dictionary(self) -> dict:
        return {
            "product": {
                "title": self.product.title,
                "price": self.product.price,
                "is_top": self.product.is_top,
                "photo": self.product.photo.url
            },
            "count": self.count
        }


# Create your models here.
class Order(models.Model):
    products: list = models.JSONField(default=[])  # {"product_id": int, "count": int}
    user = models.ForeignKey(get_user_model(), related_name='orders', on_delete=models.CASCADE)

    class StatusMeta(models.TextChoices):
        PENDING = "На проверке", gettext_lazy("PENDING")
        ACCEPT = "Принят", gettext_lazy("ACCEPT")
        PRODUCED = "Изготавливается", gettext_lazy("PRODUCED")
        ISSUED = "Выдан", gettext_lazy("ISSUED")

    status = models.CharField(
        max_length=30,
        choices=StatusMeta.choices,
        default=StatusMeta.PENDING
    )

    contact_data = models.JSONField(null=False, blank=None)

    objects: QuerySet["Order"]

    def get_products(self) -> list[_ProductModel]:
        products = []
        for product_base in Product.objects.filter(id__in=(_['id'] for _ in self.products)):
            for _ in self.products:
                if _['id'] == product_base.id:
                    products.append(_ProductModel(
                        product=product_base,
                        count=_['count']
                    ))
        return products

from django.db import models
from tortoise.queryset import QuerySet


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена')

    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to="photos/%Y/%m/%d/"
    )

    objects: QuerySet

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.title} | {self.price:,}тг"

    @property
    def string_price(self):
        return f"{self.price:,}".replace(",", ".")

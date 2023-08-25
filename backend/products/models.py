from django.db import models
from django.db.models import QuerySet


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    objects: QuerySet

    def get_photo_url(self):
        return self.photo.url

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.title} | {self.price:,}тг"

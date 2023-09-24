from django.db import models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена')

    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to="photos/%Y/%m/%d/"
    )

    class CategoriesChoices(models.TextChoices):
        CATEGORY_1 = "Ароматизированные", gettext_lazy("X1")
        CATEGORY_2 = "Ещё какие-то", gettext_lazy("X2")

    category = models.CharField(
        max_length=30,
        choices=CategoriesChoices.choices,
        default=CategoriesChoices.CATEGORY_1,
        verbose_name='Категория'
    )

    is_top = models.BooleanField(default=False, verbose_name='Отображать на главной странице')
    is_published = models.BooleanField(default=True, verbose_name='Отображать на сайте каталога')

    objects: QuerySet['Product']

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"{self.title} | {self.price:,}тг"



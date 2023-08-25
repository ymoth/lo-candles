from django.db import models
from django.db.models import QuerySet


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()

    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    objects: QuerySet

    def get_photo_url(self):
        return self.photo.url


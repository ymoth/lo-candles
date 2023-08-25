import os

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def photo_image_return(
        request: HttpRequest,
        year: str,
        month: str,
        day: str,
        photo_name: str
):
    with open(os.path.abspath('') + f'\\photos\\{year}\\{month}\\{day}\\{photo_name}', "rb") as current_image:
        return HttpResponse(current_image.read(), content_type='image/jpeg')

"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import path
from django.urls.conf import include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from config import settings
from config.contacts import GetContacts
from config.logout import LogoutView
from confirm_email.views import accessing_email
from products.views import photo_image_return


def index_handler(request: HttpRequest):
    return redirect("https://aromatic.kz/")


urlpatterns = [
    path('', index_handler),
    path('private/admin/', admin.site.urls, name='admin'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('photos/<int:year>/<str:month>/<str:day>/<str:photo_name>', photo_image_return),
    path('api/v1/logout', LogoutView.as_view(), name='logout'),
    path('api/v1/contacts', GetContacts.as_view(), name='contacts'),

    # Included lib's
    path('api/v1/', include('users.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/orders/', include('orders.urls')),
    path('api/v1/cart-system/', include('trash.urls')),
    path('confirmEmail/<str:b64data>', accessing_email)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

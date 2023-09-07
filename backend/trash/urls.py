from django.urls import path

from trash.views import CartHandler

urlpatterns = [
    path('edit/', CartHandler.as_view(), name='edit_trash'),
]

from django.urls import path

from trash.views import CartHandler, TestAPIView

urlpatterns = [
    path('edit/', CartHandler.as_view(), name='edit_trash'),
    path('test/', TestAPIView.as_view())
]

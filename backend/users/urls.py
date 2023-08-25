from django.urls import path
from .views import RegisterUserView, login, CurrentLoggedInUser, GetUsersList

urlpatterns = [
    path('login', login),
    path('register', RegisterUserView.as_view(), name="register"),
    path('user', CurrentLoggedInUser.as_view({'get': 'retrieve'}), name="current_user"),
    path('users', GetUsersList.as_view(), name="current_user"),
]


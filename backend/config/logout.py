import contextlib
from pprint import pprint

from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: HttpRequest):
        return Response(status=status.HTTP_200_OK, data={"success": "Вы успешно вышли из системы"})
        # try:
        #     if request.headers.get('Authorization'):
        #         refresh_token = request.headers.get('Authorization').replace("Bearer ", "")
        #         print(f"{refresh_token=!r}")
        #
        #         _model = RefreshToken(refresh_token)
        #         _model.blacklist()
        #         return Response(status=status.HTTP_200_OK, data={"success": "Вы успешно вышли из системы"})
        #     else:
        #         return Response(status=status.HTTP_400_BAD_REQUEST, data={"refresh_token": ["Обязательное значеник"]})
        # except Exception as e:
        #     print(e)
        #     return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"error": ["Server error"]})

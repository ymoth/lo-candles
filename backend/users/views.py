import json
import random
import smtplib
import typing

import django.contrib.auth.password_validation
from django.http import HttpRequest
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    ListAPIView
)

from django.contrib.auth import get_user_model
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny
)
from rest_framework.serializers import Serializer

from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView

from confirm_email.models import ConfirmedEmail
from .models import User
from .serializers import (
    UserSerializer,
    UserListSerializer
)

from rest_framework.decorators import api_view, throttle_classes
from rest_framework import (
    exceptions,
    status, serializers, validators,
)

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import ModelViewSet
import requests


def password_validator(value: str) -> typing.NoReturn | str:
    if len(value) < 8 or len(value) > 30:
        raise ValidationError("В пароле должно быть не менее 8 символов и не должно превышать 30 символов. ")
    return value


class RegisterSerializer(Serializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True, min_length=1, max_length=10),
    last_name = serializers.CharField(required=True, min_length=1, max_length=10),
    password = serializers.CharField(required=True, validators=[password_validator])


class RegisterUserView(APIView):
    throttle_classes = [UserRateThrottle]
    permission_classes = (AllowAny,)

    def post(self, request: HttpRequest) -> Response:
        data = json.loads(request.body)

        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(status=400, data=serializer.errors)

        user = User.objects.filter(email=data['email']).first()
        if user is not None:
            return Response(
                status=status.HTTP_409_CONFLICT,
                data={"email": ["Пользователь с такой учетной записей уже зарегистрирован"]}
            )
        confirm_email = ConfirmedEmail.objects.create(
            access_code=ConfirmedEmail.generate_email_code(),
            user_data=data,
            email=data['email']
        )
        try:
            confirm_email.send_email_code()
        except smtplib.SMTPException:
            return Response(status=400, data={
                "error": [
                    f"SMTP server was unable to send an email to this email `{data['email']}`"
                ]
            })
        except Exception as ex:
            return Response(status=400, data={
                "error": [
                    f"{ex}"
                ]
            })
        return Response(status=200, data={
            "response": [
                f"An email has been sent to the user. Code: {random.randint(1000, 4001)}"
            ],
            "payload": data
        })


class GetUsersList(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserListSerializer


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = get_user_model().objects.filter(email=email).first()
    if user is None:
        raise exceptions.AuthenticationFailed('Пользователь не найден')

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed('Не верный пароль')

    response = Response()
    token_endpoint = reverse(viewname='token_obtain_pair', request=request)
    tokens = requests.post(token_endpoint, data=request.data).json()
    response.data = {
        'access_token': tokens.get('access'),
        'refresh_token': tokens.get('refresh'),
        'email': user.email
    }
    return response


@api_view(["POST"])
@throttle_classes([UserRateThrottle])
def resset_user_password(request: HttpRequest) -> Response:
    align_items = ['email', 'new_password']
    query_payload = json.loads(request.body)
    print(query_payload.keys, align_items)
    if list(query_payload.keys()) != align_items:
        return Response(status=400, data={"error": ["Incorrect payload"]})

    user = User.objects.filter(email=query_payload['email']).first()
    if user is None:
        return Response(
            status=status.HTTP_409_CONFLICT,
            data={"error": ["Пользователь с такой учетной записью не существует. "]}
        )
    else:
        confirm_email = ConfirmedEmail.objects.create(
            access_code=ConfirmedEmail.generate_email_code(),
            user_data=query_payload,
            email=query_payload['email']
        )
        try:
            confirm_email.send_email_code()
        except:
            return Response(status=400, data={
                "error": [
                    f"SMTP server was unable to send an email to this email `{query_payload['email']}`"
                ]
            })
        return Response(status=200, data={
            "response": [
                f"An email has been sent to the user. Code: {random.randint(1000, 4001)}"
            ],
            "payload": query_payload
        })


class CurrentLoggedInUser(ModelViewSet):
    queryset = get_user_model().objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user_profile = self.queryset.get(email=request.user.email)
        serializer = self.get_serializer(user_profile)
        return Response({'user': serializer.data})

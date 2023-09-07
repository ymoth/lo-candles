"""
ASGI config for go2trip_test project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import base64
import json
import os
import typing
from typing import TypeVar

import aiohttp
import loguru
from channels.auth import AuthMiddlewareStack
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.routing import ProtocolTypeRouter, URLRouter

from django.urls import path, re_path

from confirm_email.views import SMTPMailer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'go2trip_test.settings')

T = TypeVar("T", bound=typing.Dict[typing.Literal['dict'], typing.Any])


class UserReceiver(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.room_group_name = None
        self.user_id = None

    async def connect(self):
        # Получаем нужный сервис для обработки событий на нужной базе отдыха
        self.user_id = str(self.scope['url_route']['kwargs']['user_id'])
        self.room_group_name = "user-event-system-%s" % self.user_id
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        payload_data = json.loads(text_data or bytes_data)
        await self.channel_layer.group_send(
            group=self.room_group_name,
            message={"type": f"type_{payload_data['type']}", "payload": payload_data}
        )

    # New event : book is created
    async def type_accessing_user(self, payload: T, **extra):
        """
        Обработчик входного соединения, после создании новой брони обрабатывается нужный канал,
        определяемый по сервису (который ставится в index.html (JS) let service = {{ service }}; ).

        При создании новой брони, обрабатывается в самом JS
        socket.onmessage = (event) => {
            let data = JSON.parse(event.data)
            if (data.type === "new_message") { messages.push(data.message) }
        }
        """
        loguru.logger.info(f'Passed payload: {payload} | Service: {self.user_id}')
        await self.send(text_data=json.dumps(payload))

    async def type_new_notification_user(self, payload: T, **extra):
        await self.send(text_data=json.dumps(payload))


class UserRegister(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.payload: str = ""
        self.room_group_name = None
        self.session = None

    async def connect(self):
        # Получаем нужный сервис для обработки событий на нужной базе отдыха
        self.payload = str(self.scope['url_route']['kwargs']['payload'])
        self.session = "x-1"
        self.room_group_name = "registering-system%s" % self.session

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        payload_data = json.loads(text_data or bytes_data)
        print(f'new receive: {payload_data}')
        await self.channel_layer.group_send(
            group=self.room_group_name,
            message={"type": f"type_{payload_data['type']}", "payload": payload_data}
        )

    async def type_send_email_code(self, payload: T) -> None:
        try:
            smtp_server = SMTPMailer(email=self._base64_read_data()['email'])
            smtp_server.answer_access_type(self.payload, decoded=self._base64_read_data())
            await self.send(text_data=json.dumps({"success": "send code"}))
        except Exception as ex:
            await self.send(text_data=json.dumps({"error": f"{ex}"}))

    async def type_success_connection(self, payload: T, **extra) -> None:
        """
        Сама сессия создаётся в base64 формате JSON {"emai": "...", "password": "..."}
        После чего коннектится нужная сессия в wss на стороне фронтенда.

        При подтверждении самой почты будет открываться новая вкладка у пользователя с подтверждением.
        При открытии вкладки отсылается запрос на стороне бекенда на веб сокет, при успешной дате отправляется
        новый ивент на сам фронтенд с декоденым base64.
        """

        print("AAAAAAA", self._base64_read_data())

        async with aiohttp.ClientSession() as session:
            async with session.post(
                    'https://dev.aromatic.kz/api/v1/registering_user_sys/',
                    data=self._base64_read_data()
            ) as server_response:
                if server_response.status != 200:
                    registering_response = await server_response.json()
                    await self.send(text_data=json.dumps(registering_response, ensure_ascii=False))
                    return

        await self.send(
            text_data=json.dumps({
                "type": "confirmEmail", "data": self._base64_read_data()
            })
        )

    def _base64_read_data(self) -> dict:
        """
        Read a base64 data with self connection
        TODO: return: {"email": "iam@aromatic.kz", "password": "pass"}
        """
        return json.loads(base64.b64decode(bytes(self.payload.encode('utf-8'))))


websocket_urlpatterns = [
    path(r'ws/user-system/<int:user_id>/', UserReceiver.as_asgi()),
    path(r'auth/register/<str:payload>/', UserRegister.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

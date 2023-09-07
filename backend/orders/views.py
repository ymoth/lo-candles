import asyncio
import json
import traceback

from aiogram import types
from asgiref.sync import sync_to_async
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from config.mics import bot, ADMIN_TELEGRAM_ID
from orders.models import Order
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class GetListOrders(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: HttpRequest):
        queryset = Order.objects.filter(user=request.user)
        return Response(
            status=status.HTTP_200_OK, data={
                "count": len(queryset),
                "items": [
                    {
                        "order": product_model.id,
                        "status": product_model.status,
                        "data": [base.as_dictionary() for base in product_model.get_products()]
                    }
                    for product_model in queryset
                ]
            }
        )


async def new_order_answer_to_telegram(order: Order):
    await bot.send_message(
        chat_id=ADMIN_TELEGRAM_ID,
        text=f"""
        Новый заказ для пользователя {order.contact_data['first_name'].capitalize()} {order.contact_data['last_name'].capitalize()}
        Номер телефона: {order.contact_data['phone_number']}
        
        """.replace(" " * 4, ""),
        reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton(
            text='Посмотреть заказ',
            url=f'https://dev.aromatic.com/orders/<{order.user.id}>/<{order.id}>/'
        ))
    )


class CreateOrder(APIView):
    permission_classes = (IsAuthenticated,)
    values = {
        'request_params': {'payload_products': 'Обязательное поле', 'contact_data': 'Обязательное поле'},
        'payload_products': {'id': int, 'count': int},
        'contact_data': {'first_name': str, 'last_name': str, 'phone_number': str}
    }

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        if not json.loads(request.body).keys() == self.values['request_params'].keys():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "Invalid request", "data": self.values['request_params']}
            )

        is_success_products, response_products = self.check_payload_products(request)
        is_success_contact_data, response_contact_data = self.check_payload_contact_data(request)
        if not is_success_products:
            return response_products
        if not is_success_contact_data:
            return response_contact_data

        order = Order.objects.create(
            products=response_products,
            user=request.user,
            contact_data=response_contact_data
        )
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "response": "success",
                "order": order.id,
                "status": order.status,
                "data": [base.as_dictionary() for base in order.get_products()]
            }
        )

    def check_payload_products(self, request: HttpRequest) -> tuple[bool, Response | list[dict[str, int]]]:
        """
        CHECK PAYLOAD PRODUCTS: TODO: VALUES
        -> list[ {"id" Integer(Required), "count": int} ]
        """
        try:
            payload_products = json.loads(request.body)['payload_products']
            if isinstance(payload_products, list):
                for product in payload_products:
                    if not self.values['payload_products'].keys() == product.keys():
                        return False, Response(
                            status=status.HTTP_400_BAD_REQUEST,
                            data={"error": {"title": "Обязательные поля",
                                            "values": self.values['payload_products'].keys()}}
                        )
                    if (
                            not isinstance(product['id'], self.values['payload_products']['id']) or
                            not isinstance(product['count'], self.values['payload_products']['count'])
                    ):
                        return False, Response(
                            status=status.HTTP_400_BAD_REQUEST,
                            data={"error": {"title": "Не верный тип данных",
                                            "values": self.values['payload_products'].keys()}}
                        )

            return True, payload_products
        except (Exception,) as ex:
            return False, Response(status=status.HTTP_400_BAD_REQUEST, data={
                "error": {
                    "title": "Не верный тип запроса", "values": self.values['payload_products'].keys(),
                    'example': r'"payload_products": [{"id": Int, "count": Int}]'
                }
            })

    def check_payload_contact_data(self, request: HttpRequest, _: str = "contact_data") -> tuple[bool, Response | dict]:
        """
        CHECK PAYLOAD CONTACT_DATA: TODO: VALUES
        """
        try:
            payload_contact_data = json.loads(request.body)['contact_data']
            for k, v in self.values[_].items():
                if payload_contact_data.get(k) is None:
                    return False, Response(status=status.HTTP_400_BAD_REQUEST, data={'error': {
                        'title': f"Обязательный параметр `{k}` не найден. ",
                        "payload": payload_contact_data[v].keys(), "required": self.values[_].keys()}
                    })
                if not isinstance(payload_contact_data[k], self.values[_][k]):
                    return False, Response(status=status.HTTP_400_BAD_REQUEST, data={'error': {
                        'title': f"Тип данных ключа `{k}` не поддерживает нужный тип данных `String`. ",
                        "extra": self.values[_].keys()}
                    })
            return True, payload_contact_data
        except (Exception,) as ex:
            traceback.print_exc()
            return False, Response(status=status.HTTP_400_BAD_REQUEST, data={
                "error": {
                    "title": "Не верный тип запроса", "values": self.values['contact_data'].keys(),
                    'example': r'{"contact_data": {"first_name": String, "last_name": String, "phone_number": String}}',
                    'err': str(ex)
                }
            })

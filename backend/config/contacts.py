import rest_framework.response
from django.http import HttpRequest
from rest_framework.views import APIView


class GetContacts(APIView):
    def get(self, request: HttpRequest):
        """Получение данных контактов"""
        return rest_framework.response.Response(
            status=200,
            data={
                "status": "success",
                "contacts": {
                    "instagram": "https://www.instagram.com/aromatic_svechi/",
                    "whatsapp": "https://wa.me/+77787747039",
                    "telegram": "https://t.me/+77787747039",
                }
            }
        )

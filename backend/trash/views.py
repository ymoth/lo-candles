import json

from django.http import HttpRequest
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class CartHandler(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request: HttpRequest) -> Response:
        try:
            query_data: dict[str, dict[str, int]] = json.loads(request.body)
            for item, value in query_data.items():
                if value['count'] > 200 or value['count'] < 1:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST, data={
                            "error": "The number of items under the number "
                                     f"`{item}` must be no more than 200 or no less than 1"
                        })
            request.user.cart_data = query_data
            request.user.save()
            return Response(
                status=status.HTTP_200_OK,
                data={"response": {
                    "message": "Success set value to user",
                    "data": query_data}
                }
            )
        except Exception as ex:
            return Response(
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                data={
                    "error": "Invalid request"
                }
            )

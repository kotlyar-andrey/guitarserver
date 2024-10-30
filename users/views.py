import uuid

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import MobileUser, Payment


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print("data: ", request.data)
        user_id = request.data.get('user_id')
        os = request.data.get("os")
        purchases = request.data.get("purchases")
        if user_id:
            user, created = MobileUser.objects.get_or_create(uuid=user_id, os=os)
            if purchases and isinstance(purchases, list):
                for purchase in purchases:
                    payment = Payment(mobile_user=user, info=purchase)
                    payment.save()
        return Response(status=status.HTTP_200_OK)


class NewPurchase(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        print("data: ", request.data)
        return Response(status=status.HTTP_200_OK)
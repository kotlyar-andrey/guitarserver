from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import MobileUser, Payment
from guitarserver.config import check_purchase


class Register(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
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
        purchase = request.data.get("purchase")
        user_id = request.data.get("user_id")
        os = request.data.get("os")
        if purchase and user_id:
            product_id = purchase.get("productId")
            token = purchase.get("purchaseToken")
            result = check_purchase(product_id, token)
            if result:
                user, created = MobileUser.objects.get_or_create(uuid=user_id, os=os)
                payment = Payment(mobile_user=user, info=purchase, checked=True,
                                  product_id=purchase.get("productId"),
                                  transaction_id=purchase.get("transactionId"))
                payment.save()
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

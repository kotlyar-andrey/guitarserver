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
        # try:
        user_id = request.data.get('user_id')
        os = request.data.get("os")
        purchases = request.data.get("purchases")
        print("received data: ", user_id, os, purchases)
        if user_id:
            user, created = MobileUser.objects.get_or_create(uuid=user_id, os=os)
            print("user got or created: ", user, created)
            user.os = os
            print("user: ", user)
            if purchases:
                for purchase in purchases:
                    payment = Payment(mobile_user=user, info=purchase)
                    payment.save()
                    print("saved purchase:", payment)
        return Response(status=status.HTTP_200_OK)
        # except:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import Register, NewPurchase

urlpatterns = [
    path('init-receive/', Register.as_view(), name='init_receive'),
    path('new-purchase/', NewPurchase.as_view(), name='new_purchase')
]
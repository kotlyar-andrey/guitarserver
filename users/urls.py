from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import Register

urlpatterns = [
    path('init-receive/', Register.as_view(), name='init_receive'),
]

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import Register

urlpatterns = [
    path('receive/', Register.as_view(), name='register'),
]

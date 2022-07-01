from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import User


class UserAuthTest(APITestCase):
    """
    Регистрация и авторизация пользователя, токены и профиль
    """

    def setUp(self):
        self.test_user = User.objects.create(email="t@t.com")
        self.test_user.set_password("123")
        self.test_user.save()

    def test_registration(self):
        url = reverse("register")
        response = self.client.post(url, data={"email": "t1@t.com", "password": 123, "password2": 123})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("user", response.data)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)
        self.assertFalse(response.data["user"]["is_premium"])

    def test_login(self):
        url = reverse("token_create")
        response = self.client.post(url, data={"email": "t@t.com", "password": "123"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("refresh", response.data)
        self.assertIn("access", response.data)

    def test_refresh(self):
        url = reverse("token_refresh")
        refresh_token = str(RefreshToken.for_user(self.test_user))
        response = self.client.post(url, data={"refresh": refresh_token})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

    def test_profile(self):
        url = reverse("profile")
        access_token = str(RefreshToken.for_user(self.test_user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("pk", response.data)
        self.assertIn("email", response.data)
        self.assertIn("is_premium", response.data)
        self.assertIn("settings", response.data)
        self.assertIn("progress", response.data)

    def test_profile_error(self):
        url = reverse("profile")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, {"detail": "Учетные данные не были предоставлены."})

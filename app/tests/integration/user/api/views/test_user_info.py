from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from tests.utils.factories import UserFactory


class TestUserMeAPIView(APITestCase):
    def setUp(self):
        self.user = UserFactory(image="profile.png")
        self.url = reverse("user_me_api")
        self.client = APIClient()

    def authenticate(self):
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_authenticated_user_gets_own_data(self):
        self.authenticate()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["full_name"], self.user.get_full_name())
        self.assertEqual(response.data["image"], self.user.image.url)

    def test_authenticated_user_gets_data_when_no_image(self):
        self.user = UserFactory(image=None, email="testuser@gmail.com")
        self.authenticate()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["image"], "/static/images/user.png")

    def test_unauthenticated_user_gets_401(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from tests.factories.user_factory import UserFactory


class TestAPIUrls(APITestCase):

    def authenticate(self):
        user = UserFactory()
        refresh = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        return user

    def test_register_api_get_not_allowed(self):
        url = reverse('register_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_custom_token_obtain_pair_api_get_not_allowed(self):
        url = reverse('custom_token_obtain_pair')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_token_refresh_api_get_not_allowed(self):
        url = reverse('custom_token_refresh')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_user_api_post_not_allowed(self):
        self.authenticate()
        url = reverse('user_me_api')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_logout_api_get_not_allowed(self):
        self.authenticate()
        url = reverse('logout_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

import datetime

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from tests.utils.factories import UserFactory


class TestLogoutAPIView(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.url = reverse('logout_api')

    def authenticate(self):
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.refresh_token = str(refresh)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_successful_logout_blacklists_token(self):
        self.authenticate()
        self.client.cookies['refresh_token'] = self.refresh_token
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_logout_fails_with_missing_refresh_token(self):
        self.authenticate()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_fails_with_invalid_refresh_token(self):
        invalid_tokens = ['invalid_token', '', None]
        for token in invalid_tokens:
            with self.subTest(token=token):
                self.authenticate()
                self.client.cookies['refresh_token'] = token
                response = self.client.post(self.url)
                self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_fails_with_expired_refresh_token(self):
        self.authenticate()
        expired_refresh = RefreshToken(self.refresh_token)
        expired_refresh.set_exp(lifetime=datetime.timedelta(seconds=-1))
        self.client.cookies['refresh_token'] = str(expired_refresh)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_fails_without_authentication(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_fails_with_invalid_access_token(self):
        self.authenticate()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid_token')
        self.client.cookies['refresh_token'] = self.refresh_token
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_logout_fails_with_blacklisted_refresh_token(self):
        self.authenticate()
        refresh = RefreshToken(self.refresh_token)
        refresh.blacklist()
        self.client.cookies['refresh_token'] = str(refresh)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_fails_with_blacklisted_access_token(self):
        self.authenticate()
        refresh = RefreshToken(self.refresh_token)
        refresh.blacklist()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_fails_with_inactive_user(self):
        self.authenticate()
        self.client.cookies['refresh_token'] = self.refresh_token
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_double_logout(self):
        self.authenticate()
        self.client.cookies['refresh_token'] = self.refresh_token
        self.client.post(self.url)  # First logout
        response = self.client.post(self.url)  # Second logout
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_logout_clears_refresh_cookie(self):
        self.authenticate()
        self.client.cookies['refresh_token'] = self.refresh_token
        response = self.client.post(self.url)
        refresh_cookie = response.cookies.get('refresh_token')
        self.assertIsNotNone(refresh_cookie)
        self.assertEqual(refresh_cookie.value, '')
        self.assertEqual(refresh_cookie['max-age'], 0)

    def test_logout_fails_with_tampered_refresh_token(self):
        self.authenticate()
        tampered = self.refresh_token[:-1] + 'a'
        self.client.cookies['refresh_token'] = tampered
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

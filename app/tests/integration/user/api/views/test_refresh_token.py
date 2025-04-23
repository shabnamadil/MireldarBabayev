import datetime

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from tests.factories.user_factory import UserFactory


class TestCustomTokenRefreshView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.refresh_url = reverse('custom_token_refresh')
        self.obtain_url = reverse('custom_token_obtain_pair')
        self.data = {
            'email': self.user.email,
            'password': 'testpassword',
        }

    def test_refresh_token_not_found_in_cookie(self):
        response = self.client.post(self.refresh_url, self.data, format='json')
        refresh_token_cookie = response.cookies.get('refresh_token')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(refresh_token_cookie)
        self.assertEqual(
            response.data,
            {'detail': 'Refresh token not found in cookie'},
        )

    def test_refresh_token_found_in_cookie(self):
        response = self.client.post(self.obtain_url, self.data, format='json')
        refresh_token_cookie = response.cookies.get('refresh_token')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(refresh_token_cookie)

    def test_refresh_token_returns_new_access_token(self):
        response = self.client.post(self.obtain_url, self.data, format='json')
        refresh_token_cookie = response.cookies.get('refresh_token')

        # Use the refresh token to get a new access token
        refresh_response = self.client.post(
            self.refresh_url,
            {'refresh': refresh_token_cookie.value},
            format='json',
        )
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', refresh_response.data)

    def test_expired_refresh_token_returns_401(self):
        refresh_token = RefreshToken.for_user(self.user)
        refresh_token.set_exp(lifetime=datetime.timedelta(seconds=-1))
        self.client.cookies['refresh_token'] = str(refresh_token)
        response = self.client.post(self.refresh_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(
            response.data['detail'], 'Invalid or expired refresh token'
        )

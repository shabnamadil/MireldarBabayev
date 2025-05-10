from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from tests.factories.user_factory import UserFactory


class TestCustomTokenObtainPairView(APITestCase):

    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('custom_token_obtain_pair')
        self.data = {
            'email': self.user.email,
            'password': 'testpassword',
        }

    def test_token_obtain_pair_returns_no_token_in_response(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, None)

    def test_token_obtain_pair_with_refresh_token_in_cookie(self):
        response = self.client.post(self.url, self.data, format='json')

        """ Check that the refresh token is in the HttpOnly cookie (secure and
        samesite properties) """
        refresh_token_cookie = response.cookies.get('refresh_token')
        self.assertIsNotNone(refresh_token_cookie)
        self.assertTrue(refresh_token_cookie['httponly'])
        self.assertTrue(refresh_token_cookie['secure'])
        self.assertEqual(refresh_token_cookie['samesite'], 'Lax')

    def test_token_obtain_pair_with_invalid_credentials(self):
        data = {
            'email': 'wronguser@gmail.com',
            'password': 'WrongPass123!',
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_obtain_pair_with_missing_fields(self):
        data = {'email': '', 'password': ''}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertIn('password', response.data)

    def test_token_obtain_pair_with_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

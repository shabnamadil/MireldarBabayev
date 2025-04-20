from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase

from apps.user.middleware import CurrentUserMiddleware, get_current_user

User = get_user_model()


class TestCurrentUserMiddleware(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.middleware = CurrentUserMiddleware(lambda r: r)

    def test_get_current_user_returns_request_user(self):
        user = User(email='test@example.com')
        request = self.factory.get('/')
        request.user = user

        self.middleware(request)

        self.assertEqual(get_current_user(), user)

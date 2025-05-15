from django.test import TestCase
from django.urls import reverse


class TestLoginPageView(TestCase):

    def test_login_page_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'login.js')
        self.assertTemplateUsed(response, 'components/user/login/login.html')

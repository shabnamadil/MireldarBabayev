from django.test import TestCase
from django.urls import reverse


class TestRegisterPageView(TestCase):
    def test_register_page_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'register.js')
        self.assertTemplateUsed(response, 'components/user/register/register.html')

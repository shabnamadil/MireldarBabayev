from django.test import TestCase
from django.db.utils import IntegrityError

from apps.core.models import Faq


class TestFaqModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.faq = Faq.objects.create(
            question='Faq question',
            response='Faq response'
        )

    def test_str_method(self):
        self.assertEqual(str(self.faq), "Faq question")

    def test_question_response_unique(self):
        with self.assertRaises(IntegrityError):
            Faq.objects.create(
                question='Faq question',
                response='Faq response'
            )
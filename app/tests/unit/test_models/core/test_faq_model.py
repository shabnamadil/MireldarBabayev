from django.db.utils import IntegrityError

from apps.core.models import Faq
from utils.tests.base import BaseValidationTest


class TestFaqModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.faq = Faq.objects.create(
            question='Faq question',
            response='Faq response'
        )

    def test_faq_model(self):
        self.assert_model_instance(Faq, 'question', 'Faq question')
        self.assert_model_instance(Faq, 'response', 'Faq response')

    def test_question_response_unique(self):
        with self.assertRaises(IntegrityError):
            Faq.objects.create(
                question='Faq question',
                response='Faq response'
            )

    def test_str_method(self):
        self.assert_str_method(self.faq, 'Faq question')

    def test_object_count(self):
        self.assert_object_count(Faq, 1)
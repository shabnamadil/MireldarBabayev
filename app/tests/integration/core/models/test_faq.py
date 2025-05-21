from django.db import IntegrityError

from apps.core.models import Faq
from tests.utils.factories import FaqFactory
from tests.utils.helpers import (
    BaseValidationTest,
)


class TestFaqModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = FaqFactory
        cls.object = cls.factory()
        cls.model = Faq

    def test_question_required(self):
        self.assert_required_field(self.object, "question")

    def test_response_required(self):
        self.assert_required_field(self.object, "response")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_question_saved_correctly(self):
        self.assert_model_instance(self.object, "question", self.object.question)

    def test_response_saved_correctly(self):
        self.assert_model_instance(self.object, "response", self.object.response)

    def test_object_is_instance_of_faq(self):
        self.assertIsInstance(self.object, self.model)

    def test_unique_together(self):
        with self.assertRaises(IntegrityError):
            self.factory(question=self.object.question, response=self.object.response)

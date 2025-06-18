from apps.core.models import Faq
from tests.utils.helpers import BaseValidationTest


class TestFaqModel(BaseValidationTest):

    def test_faq_str_returns_question(self):
        self.assert_str_output(Faq, "question", "Test question")

from apps.service.models import Coworker
from utils.tests.base import BaseValidationTest


class TestCoworkerModel(BaseValidationTest):

    def test_coworker_str_returns_name(self):
        self.assert_str_output(Coworker, 'name', 'Test coworker')

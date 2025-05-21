from apps.core.models import StatisticalIndicator
from tests.utils.helpers import BaseValidationTest


class TestStatisticalIndicatorModel(BaseValidationTest):

    def test_indicator_str_returns_title(self):
        self.assert_str_output(StatisticalIndicator, "name", "Test name")

from apps.blog.models import Category
from tests.utils.helpers import BaseValidationTest


class TestCategoryModel(BaseValidationTest):

    def test_category_str_returns_name(self):
        self.assert_str_output(Category, "name", "Test category")

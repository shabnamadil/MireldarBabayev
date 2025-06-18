from apps.blog.models import Tag
from tests.utils.helpers import BaseValidationTest


class TestTagModel(BaseValidationTest):

    def test_tag_str_returns_name(self):
        self.assert_str_output(Tag, "name", "Test tag")

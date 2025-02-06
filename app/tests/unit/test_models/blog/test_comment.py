from utils.tests.base import BaseValidationTest
from apps.blog.models import Comment


class TestCommentModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        cls.comment = Comment.objects.create(
            content='Test bloq',
            
        )



from utils.tests.base import BaseValidationTest
from apps.blog.models import Comment, Blog


class TestCommentModel(BaseValidationTest):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.blog = Blog.objects.create(
            title='Test bloq',
            author=cls.user
        )
        cls.comment = Comment.objects.create(
            content='Test bloq',
            blog=cls.blog,
            author=cls.user
        )


    def test_model(self):
        self.assert_model_instance(Comment, 'content', 'Test bloq')
        self.assert_model_instance(Comment, 'blog', self.blog)
        self.assert_model_instance(Comment, 'author', self.user)
        self.assert_model_instance(Comment, 'truncated_comment', 'Test bloq')

    def test_object_count(self):
        self.assert_object_count(Comment, 1)

    def test_deletion(self):
        self.assert_object_deleted(Comment)

    def test_comment_ordering(self):
        """Ensure comments are ordered by 'created_at' descending."""
        new_comment = Comment.objects.create(
            content="New comment",
            blog=self.blog,
            author=self.user,
        )

        comments = Comment.objects.all()
        self.assertEqual(comments.first(), new_comment)
        self.assertEqual(comments.last(), self.comment)

    def test_truncated_comment(self):
        """Ensure 'truncated_comment' returns only 3 words followed by '...' when needed."""
        comment = Comment.objects.create(
            content="This is a very long comment that should be truncated",
            blog=self.blog,
            author=self.user
        )
        self.assertEqual(comment.truncated_comment, "This is a ...")

    def test_str_method(self):
        self.assert_str_method(self.comment, self.comment.truncated_comment)
from apps.blog.models import Comment
from tests.utils.factories import BlogFactory, CommentFactory, UserFactory
from tests.utils.helpers import (
    BaseValidationTest,
)


class TestCommentModelIntegration(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = CommentFactory
        cls.object = cls.factory()
        cls.model = Comment

    def test_content_required(self):
        self.assert_required_field(self.object, "content")

    def test_blog_required(self):
        self.assert_required_field(self.object, "blog")

    def test_author_required(self):
        self.assert_required_field(self.object, "author")

    def test_object_count(self):
        self.assert_object_count(self.model, 1)

    def test_object_deletion(self):
        self.assert_object_deleted(self.model)

    def test_comment_content_saved_correctly(self):
        self.assert_model_instance(self.object, "content", self.object.content)

    def test_object_is_instance_of_comment(self):
        self.assertIsInstance(self.object, self.model)

    def test_comments_are_ordered_by_created_at_desc(self):
        self.assert_ordering(self.factory, self.model, "created_at")

    def test_comment_str_returns_truncated_comment(self):
        self.assert_str_output(self.model, "content", self.object.truncated_comment)

    def test_long_comment_truncated_content(self):
        comment = self.factory.create(
            content="This is a test comment with more than three words."
        )
        expected_truncated = "This is a ..."
        self.assertEqual(comment.truncated_comment, expected_truncated)

    def test_short_comment_truncated_content(self):
        short_comment = self.factory.create(content="Short comment")
        self.assertEqual(short_comment.truncated_comment, "Short comment")

    def test_comment_author_saved_correctly(self):
        self.assert_model_instance(self.object, "author", self.object.author)

    def test_author_deletion_deletes_comment(self):
        self.object.author.delete()
        self.assertEqual(Comment.objects.count(), 0)

    def test_comment_author_persistence(self):
        user = UserFactory()
        comment = CommentFactory(author=user)
        self.assertEqual(comment.author, user)

    def test_comment_blog_saved_correctly(self):
        self.assert_model_instance(self.object, "blog", self.object.blog)

    def test_blog_deletion_deletes_comment(self):
        self.object.blog.delete()
        self.assertEqual(Comment.objects.count(), 0)

    def test_comment_blog_persistence(self):
        blog = BlogFactory()
        comment = CommentFactory(blog=blog)
        self.assertEqual(comment.blog, blog)

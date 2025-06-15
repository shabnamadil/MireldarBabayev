from unittest.mock import patch

from django.core import mail

from tests.utils.factories import CommentFactory, UserFactory
from tests.utils.helpers import (
    BaseValidationTest,
)


class TestCommentSignal(BaseValidationTest):
    @classmethod
    def setUpTestData(cls):
        cls.factory = CommentFactory
        cls.object = cls.factory()
        cls.admin_user = UserFactory(is_staff=True, is_superuser=True)

    @patch("apps.blog.signals.get_current_user")
    def test_notify_user_on_comment_delete_by_admin_sends_email(
        self, mock_get_current_user
    ):
        mock_get_current_user.return_value = self.admin_user

        self.object.delete()

        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertIn("Your comment has been deleted", email.subject)
        self.assertIn(self.object.content, email.body)
        self.assertIn(self.object.blog.title, email.body)
        self.assertIn(self.object.author.email, email.to)

    @patch("apps.blog.signals.get_current_user")
    def test_signal_does_not_send_email_if_deleted_by_author(
        self, mock_get_current_user
    ):
        mock_get_current_user.return_value = self.object.author

        self.object.delete()
        self.assertEqual(len(mail.outbox), 0)

    @patch("apps.blog.signals.get_current_user")
    def test_signal_does_not_send_email_if_author_is_staff(self, mock_get_current_user):
        staff_user = UserFactory(is_staff=True)
        comment = CommentFactory(author=staff_user)
        mock_get_current_user.return_value = comment.author

        comment.delete()
        self.assertEqual(len(mail.outbox), 0)

    @patch("apps.blog.signals.get_current_user")
    def test_signal_does_not_send_email_if_no_current_user(self, mock_get_current_user):
        mock_get_current_user.return_value = None
        self.object.delete()
        self.assertEqual(len(mail.outbox), 0)

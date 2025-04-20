from django.test import TestCase

from apps.user.forms import LoginForm


class TestLoginForm(TestCase):

    def test_login_form_valid_data(self):
        form_data = {
            'email': 'user@example.com',
            'password': 'strongpassword123',
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_login_form_missing_email(self):
        form_data = {'password': 'strongpassword123'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_login_form_invalid_email_format(self):
        form_data = {'email': 'invalid-email', 'password': 'strongpassword123'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_login_form_missing_password(self):
        form_data = {'email': 'user@example.com'}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors)

    def test_login_form_blank_fields(self):
        form_data = {'email': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertIn('password', form.errors)

    def test_email_field_widget_attrs(self):
        form = LoginForm()
        self.assertEqual(
            form.fields['email'].widget.attrs['placeholder'],
            'Enter your email',
        )
        self.assertIn(
            'form-control', form.fields['email'].widget.attrs['class']
        )

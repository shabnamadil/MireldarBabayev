from tests.factories.user_factory import UserFactory
from tests.slow.web_ui.helpers.base_test import BaseTest
from tests.slow.web_ui.helpers.translations import TRANSLATIONS
from tests.slow.web_ui.pages.register_page import RegisterPage


class RegisterPageTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.register_page = RegisterPage(self.browser)

    def test_register_page_loads_in_multilinguage(self):
        for lang in TRANSLATIONS.keys():
            with self.subTest(language=lang):
                self.register_page.load(self.live_server_url, lang)

                translations = TRANSLATIONS[lang]

                self.assertIn(
                    translations['Create Your Account'],
                    self.browser.page_source,
                )

    def test_successful_register_with_full_data(self):
        """Image content is handled in register POM"""
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhondoe@gmail.com',
            '',
            'jhondoe1234',
            'jhondoe1234',
        )
        success_message = self.register_page.get_text(RegisterPage.success_message)
        self.assertIn('You successfully registered.', success_message)
        self.register_page.wait_url_changes(self.browser.current_url)
        self.assertIn('Sign into your account', self.browser.page_source)

    def test_successful_register_without_image(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhondoe@gmail.com',
            None,
            'jhondoe1234',
            'jhondoe1234',
        )
        success_message = self.register_page.get_text(RegisterPage.success_message)
        self.assertIn('You successfully registered.', success_message)
        self.register_page.wait_url_changes(self.browser.current_url)
        self.assertIn('Sign into your account', self.browser.page_source)

    def test_register_with_existing_email(self):
        self.register_page.load(self.live_server_url)
        existing_user = UserFactory(email='jhon@gmail.com')
        self.register_page.register(
            'Jhon',
            'Doe',
            existing_user.email,
            None,
            'jhondoe1234',
            'jhondoe1234',
        )
        error_message = self.register_page.get_error_message('email')
        self.assertIn('This email is already registered', error_message)

    def test_register_with_invalid_email_format(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'invalidemail',
            None,
            'jhondoe1234',
            'jhondoe1234',
        )
        email_input = self.register_page.find_element(RegisterPage.email_input)
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", email_input
        )
        self.assertIn(
            "Please include an '@' in the email address",
            validation_message,
        )

    def test_register_with_empty_first_name(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            '', 'Doe', 'jhoingmail.com', None, 'jhondoe1234', 'jhondoe1234'
        )
        first_name_input = self.register_page.find_element(
            RegisterPage.first_name_input
        )
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", first_name_input
        )
        self.assertIn('Please fill out this field.', validation_message)

    def test_register_with_empty_last_name(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            '',
            'jhoingmail.com',
            None,
            'jhondoe1234',
            'jhondoe1234',
        )
        last_name_input = self.register_page.find_element(RegisterPage.last_name_input)
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", last_name_input
        )
        self.assertIn('Please fill out this field.', validation_message)

    def test_register_with_empty_email(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon', 'Doe', '', None, 'jhondoe1234', 'jhondoe1234'
        )
        email_input = self.register_page.find_element(RegisterPage.email_input)
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", email_input
        )
        self.assertIn('Please fill out this field.', validation_message)

    def test_register_with_empty_password(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon', 'Doe', 'jhon@gmail.com', None, '', 'jhondoe1234'
        )
        password_input = self.register_page.find_element(RegisterPage.password_input)
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", password_input
        )
        self.assertIn('Please fill out this field.', validation_message)

    def test_register_with_empty_password_confirm(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon', 'Doe', 'jhon@gmail.com', None, 'jhondoe1234', ''
        )
        password_confirm_input = self.register_page.find_element(
            RegisterPage.confirm_password_input
        )
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;",
            password_confirm_input,
        )
        self.assertIn('Please fill out this field.', validation_message)

    def test_register_passwords_do_not_match(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhon@gmail.com',
            None,
            'jhondoe1234',
            'wrongpassword',
        )
        error_message = self.register_page.get_error_message('password_confirm')
        self.assertIn('Passwords do not match.', error_message)

    def test_register_with_invalid_image(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhon@gmail.com',
            'invalid_image.txt',
            'jhondoe1234',
            'jhondoe1234',
        )
        error_message = self.register_page.get_error_message('image')
        self.assertIn(
            'Upload a valid image.',
            error_message,
        )

    def test_register_with_empty_txt_file_as_invalid_image(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhon@gmail.com',
            'empty.txt',
            'jhondoe1234',
            'jhondoe1234',
        )
        error_message = self.register_page.get_error_message('image')
        self.assertIn(
            'The submitted file is empty',
            error_message,
        )

    def test_register_with_invalid_image_valid_extension(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhon@gmail.com',
            'invalid_image.jpg',
            'jhondoe1234',
            'jhondoe1234',
        )
        error_message = self.register_page.get_error_message('image')
        self.assertIn(
            'Upload a valid image',
            error_message,
        )

    def test_register_with_valid_image_content_disallowed_txt_extension(
        self,
    ):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhon@gmail.com',
            'disallowed_image.txt',
            'jhondoe1234',
            'jhondoe1234',
        )
        error_message = self.register_page.get_error_message('image')
        self.assertIn(
            'File extension “txt” is not allowed.',
            error_message,
        )

    def test_register_with_valid_image_content_disallowed_image_extensions(
        self,
    ):
        disallowed_extentions = ['webp', 'jpf', 'xpm']
        for ext in disallowed_extentions:
            with self.subTest(extension=ext):
                self.register_page.load(self.live_server_url)
                self.register_page.register(
                    'Jhon',
                    'Doe',
                    'jhon@gmail.com',
                    f'disallowed_image.{ext}',
                    'jhondoe1234',
                    'jhondoe1234',
                )
                error_message = self.register_page.get_error_message('image')
                self.assertIn(
                    'Only JPG, PNG, and JPEG files are accepted.',
                    error_message,
                )

    def test_register_with_image_size_exceeds(self):
        self.register_page.load(self.live_server_url)
        self.register_page.register(
            'Jhon',
            'Doe',
            'jhon@gmail.com',
            'exceed_image.jpg',
            'jhondoe1234',
            'jhondoe1234',
        )
        error_message = self.register_page.get_error_message('image')
        self.assertIn(
            'Image size should not exceed 2 MB.',
            error_message,
        )

    def test_password_field_is_masked(self):
        self.register_page.load(self.live_server_url)
        password_type = self.register_page.find_element(
            RegisterPage.password_input
        ).get_attribute('type')
        self.assertEqual(password_type, 'password')

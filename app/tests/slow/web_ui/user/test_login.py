from tests.slow.web_ui.pages import BasePage, LoginPage
from tests.utils.factories import UserFactory
from tests.utils.helpers import TRANSLATIONS, BaseUITest


class LoginPageTest(BaseUITest):

    def setUp(self):
        super().setUp()

        self.login_page = LoginPage(self.browser)
        self.user = UserFactory(email='selenium@gmail.com', password='Seleniumpass1234')

    def _successful_login(self, window_size):
        self.browser.set_window_size(*window_size)
        self.login_page.load(self.live_server_url)
        self.login_page.login('selenium@gmail.com', 'Seleniumpass1234')
        self.login_page.wait_url_changes(self.browser.current_url)
        BasePage(self.browser)._set_user_info_available()
        self.assertIn('selenium@gmail.com', self.browser.page_source)
        self.assertIn('Logout', self.browser.page_source)
        self.assertNotIn('Login', self.browser.page_source)

    def test_login_page_loads_in_multilinguage(self):
        for lang in TRANSLATIONS.keys():
            with self.subTest(language=lang):
                self.login_page.load(self.live_server_url, lang)

                translations = TRANSLATIONS[lang]

                self.assertIn(translations['Login'], self.browser.page_source)
                self.assertIn(translations['Email'], self.browser.page_source)
                self.assertIn(translations['Password'], self.browser.page_source)

    def test_successful_login_on_large_screen(self):
        self._successful_login(window_size=(1920, 1080))

    def test_successful_login_on_medium_screen(self):
        self._successful_login(window_size=(1024, 768))

    def test_successful_login_on_small_screen(self):
        self._successful_login(window_size=(375, 667))

    def test_login_with_invalid_credentials(self):
        self.login_page.load(self.live_server_url)
        self.login_page.login('wronguser@gamil.com', 'wrongpass')
        error_message = self.login_page.get_text(LoginPage.login_error_message)
        self.assertIn('Invalid email or password. Please try again.', error_message)

    def test_login_with_invalid_email_format(self):
        self.login_page.load(self.live_server_url)
        self.login_page.login('invalidemail', 'Seleniumpass1234')
        email_input = self.login_page.find_element(LoginPage.email_input)
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", email_input
        )
        self.assertIn(
            "Please include an '@' in the email address",
            validation_message,
        )

    def test_login_with_empty_email(self):
        self.login_page.load(self.live_server_url)
        self.login_page.login('', 'Seleniumpass1234')
        email_input = self.login_page.find_element(LoginPage.email_input)
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", email_input
        )
        self.assertIn('Please fill out this field.', validation_message)

    def test_login_with_empty_password(self):
        self.login_page.load(self.live_server_url)
        self.login_page.login('selenium@gmail.com', '')
        password_input = self.login_page.find_element(LoginPage.password_input)
        validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", password_input
        )
        self.assertIn('Please fill out this field.', validation_message)

    def test_login_with_empty_email_and_password(self):
        self.login_page.load(self.live_server_url)
        self.login_page.submit_empty_login()
        email_input = self.login_page.find_element(LoginPage.email_input)
        password_input = self.login_page.find_element(LoginPage.password_input)
        email_validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", email_input
        )
        password_validation_message = self.browser.execute_script(
            "return arguments[0].validationMessage;", password_input
        )
        self.assertIn('Please fill out this field.', email_validation_message)
        self.assertIn('Please fill out this field.', password_validation_message)

    def test_password_field_is_masked(self):
        self.login_page.load(self.live_server_url)
        password_type = self.login_page.find_element(
            LoginPage.password_input
        ).get_attribute('type')
        self.assertEqual(password_type, 'password')

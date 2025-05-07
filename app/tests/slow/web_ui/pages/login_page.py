from urllib.parse import urljoin

from django.urls import reverse
from django.utils.translation import activate

from selenium.webdriver.common.by import By
from tests.slow.web_ui.pages.base import BasePage


class LoginPage(BasePage):
    """Page object for the login page."""

    # Locators for the login page elements
    email_input = (By.NAME, 'email')
    password_input = (By.NAME, 'password')
    login_error_message = (By.ID, 'alertLoginMessage')
    login_button = (By.XPATH, '//button[@type="submit"]')

    def load(self, live_server_url, lang='en'):
        activate(lang)
        login_url = urljoin(live_server_url, reverse('login'))
        self.open(login_url, lang)

    def login(self, email, password):
        self.input_text(self.email_input, email)
        self.input_text(self.password_input, password)
        self.click(self.login_button)

    def submit_empty_login(self):
        self.login('', '')

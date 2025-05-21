from urllib.parse import urljoin

from django.urls import reverse
from django.utils.translation import activate

from selenium.webdriver.common.by import By
from tests.slow.web_ui.pages import BasePage


class RegisterPage(BasePage):
    """Page object for the register page."""

    # Locators for the register page elements
    first_name_input = (By.NAME, "first_name")
    last_name_input = (By.NAME, "last_name")
    email_input = (By.NAME, "email")
    image_input = (By.NAME, "image")
    password_input = (By.NAME, "password")
    confirm_password_input = (By.NAME, "password_confirm")
    success_message = (By.ID, "successRegisterMessage")
    register_button = (By.XPATH, '//button[@type="submit"]')

    def load(self, live_server_url, lang="en"):
        activate(lang)
        login_url = urljoin(live_server_url, reverse("register"))
        self.open(login_url, lang)

    def register(
        self,
        first_name,
        last_name,
        email,
        image_name,
        password,
        confirm_password,
    ):
        """Fill in the registration form and submit it."""
        self.input_text(self.first_name_input, first_name)
        self.input_text(self.last_name_input, last_name)
        self.input_text(self.email_input, email)
        self.input_image(self.image_input, image_name)
        self.input_text(self.password_input, password)
        self.input_text(self.confirm_password_input, confirm_password)
        self.click(self.register_button)

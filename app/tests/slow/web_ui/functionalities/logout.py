from selenium.webdriver.common.by import By
from tests.slow.web_ui.pages.base import BasePage


class LogoutFunctionality(BasePage):
    logout_button = (By.ID, 'logoutButton')

    def logout(self):
        self.click(self.logout_button)

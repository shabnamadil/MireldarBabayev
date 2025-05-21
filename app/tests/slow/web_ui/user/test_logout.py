from tests.slow.web_ui.functionalities import LogoutFunctionality
from tests.slow.web_ui.pages import BasePage, LoginPage
from tests.utils.factories import UserFactory
from tests.utils.helpers import BaseUITest


class LogoutFunctionalityTest(BaseUITest):
    """Test class for logout functionality."""

    def setUp(self):
        super().setUp()

        self.logout = LogoutFunctionality(self.browser)
        self.login_page = LoginPage(self.browser)
        self.user = UserFactory(email="selenium@gmail.com", password="Seleniumpass1234")

    def _logout(self, window_size):
        # Set the window size
        self.browser.set_window_size(*window_size)

        # Step 1: Log in to the application
        self.login_page.load(self.live_server_url)
        self.login_page.login("selenium@gmail.com", "Seleniumpass1234")
        self.login_page.wait_url_changes(self.browser.current_url)
        BasePage(self.browser)._set_user_info_available()

        # Step 2: Verify that the user is logged in
        self.assertIn("Logout", self.browser.page_source)

        # Step 3: Perform the logout action
        self.logout.logout()
        self.logout.wait_url_changes(self.browser.current_url)
        self.assertIn("Login", self.browser.page_source)
        self.assertNotIn("Logout", self.browser.page_source)

    def test_logout_functionality_on_large_screen(self):
        self._logout(window_size=(1920, 1080))

    def test_logout_functionality_on_medium_screen(self):
        self._logout(window_size=(1024, 768))

    def test_logout_functionality_on_small_screen(self):
        self._logout(window_size=(375, 667))

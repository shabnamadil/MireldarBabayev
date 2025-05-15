from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.utils.helpers import ImageInputHelper


class BasePage:
    """Base class for common functionality shared by all pages."""

    profile_icon = (By.ID, "userInfoContainer")
    burger_menu = (By.CLASS_NAME, "navbar-toggler")

    def __init__(self, browser, timeout=5):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, timeout)

    def open(self, url, lang):
        self.browser.get(url)
        self.browser.add_cookie({'name': 'django_language', 'value': lang})
        self.browser.refresh()

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find_clickable_element(locator).click()

    def input_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def input_image(self, locator, image_name):
        element = self.find_visible_element(locator)
        element.clear()

        if image_name is None:
            return

        helper = ImageInputHelper()
        image_path = helper.get_image_path(image_name)
        element.send_keys(image_path)

    def get_text(self, locator):
        return self.find_visible_element(locator).text

    def get_error_message(self, field_name):
        """Get the error locator for a specific field."""
        locator = (By.ID, f'{field_name}_error')
        return self.find_visible_element(locator).text

    def wait_url_changes(self, old_url, timeout=15):
        WebDriverWait(self.browser, timeout).until(EC.url_changes(old_url))

    def _set_user_info_available(self):
        """Ensure the user profile menu is available regardless of screen size."""
        if self._is_medium_screen():
            self._handle_medium_screen_menu()
        elif self._is_large_screen():
            self._handle_large_screen_hover()

    def _is_medium_screen(self):
        return self._element_exists(self.burger_menu)

    def _is_large_screen(self):
        return self._element_exists(self.profile_icon)

    def _handle_medium_screen_menu(self):
        """Handles menu expansion and profile click on medium screens."""
        try:
            burger_menu = self.find_element(self.burger_menu)
            self.click(burger_menu)

            profile = self.find_element(self.profile_icon)
            self.click(profile)
        except Exception as e:
            self._log_ui_issue("Medium screen menu handling failed", e)

    def _handle_large_screen_hover(self):
        """Handles hover over profile icon on large screens."""
        try:
            profile = self.find_element(self.profile_icon)
            actions = ActionChains(self.browser)
            actions.move_to_element(profile).perform()
        except Exception as e:
            self._log_ui_issue("Large screen profile hover failed", e)

    def _element_exists(self, locator):
        try:
            self.find_visible_element(locator)
            return True
        except Exception:
            return False

    def _log_ui_issue(self, message, exception):
        print(f"[WARN] {message}: {exception}")

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """Base class for common functionality shared by all pages."""

    def __init__(self, browser, timeout=15):
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

    def get_text(self, locator):
        return self.find_visible_element(locator).text

    def wait_url_changes(self, old_url, timeout=15):
        WebDriverWait(self.browser, timeout).until(EC.url_changes(old_url))

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver

from .retry import RetryTestCase


class BaseTest(StaticLiveServerTestCase, RetryTestCase):
    """Base class for all tests."""

    def setUp(self):
        super().setUp()
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-application-cache")
        chrome_options.add_argument("--disk-cache-size=0")
        chrome_options.add_argument("--disable-cache")
        chrome_options.add_argument("--disable-offline-load-stale-cache")
        chrome_options.add_argument("--aggressive-cache-discard")

        self.browser = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.browser.delete_all_cookies()
        self.browser.quit()

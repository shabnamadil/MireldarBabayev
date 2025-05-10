import time
import unittest


class RetryTestCase(unittest.TestCase):
    def __init__(self, *args, retries=3, delay=2, **kwargs):
        super().__init__(*args, **kwargs)
        if retries < 1:
            raise ValueError("Retries must be at least 1")
        if delay < 0:
            raise ValueError("Delay cannot be negative")

        self.retries = retries
        self.delay = delay

    def run(self, result=None):
        """Retry a test case execution with specified retries and delay."""
        last_exception = None
        for attempt in range(self.retries):
            try:
                return super().run(result)
            except Exception as e:
                last_exception = e
                time.sleep(self.delay)
        if last_exception:
            raise last_exception

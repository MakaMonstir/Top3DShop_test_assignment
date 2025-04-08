from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class SafeWebElement:
    def __init__(self, driver: WebDriver, by: By, selector: str):
        self.driver = driver
        self.by = by
        self.selector = selector
        self._cached = None

    def _locate(self):
        self._cached = self.driver.find_element(self.by, self.selector)

    def text(self):
        try:
            if not self._cached:
                self._locate()
            return self._cached.text
        except StaleElementReferenceException:
            self._locate()
            return self._cached.text


class SafeWebElements:
    def __init__(self, driver: WebDriver, by: By, selector: str):
        self.driver = driver
        self.by = by
        self.selector = selector
        self._cached = None

    def _locate(self):
        self._cached = self.driver.find_elements(self.by, self.selector)

    def all(self):
        try:
            if self._cached is None:
                self._locate()
            # trigger one access to ensure validity
            _ = self._cached[0].tag_name if self._cached else None
            return self._cached
        except StaleElementReferenceException:
            self._locate()
            return self._cached

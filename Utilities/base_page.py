from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        """Find a single web element."""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None

    def find_elements(self, locator, timeout=10):
        """Find multiple web elements."""
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
            return elements
        except TimeoutException:
            print(f"Elements with locator {locator} not found within {timeout} seconds.")
            return []

    def click_element(self, locator, timeout=10):
        """Click on a web element."""
        element = self.find_element(locator, timeout)
        if element:
            element.click()

    def enter_text(self, locator, text, timeout=10):
        """Enter text into a text field."""
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)

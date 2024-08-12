from selenium.webdriver.common.by import By
from Utilities.base_page import BasePage  # Import BasePage

class ProductPage(BasePage):
    FIRST_ITEM_ADD_TO_CART_BUTTON = (By.XPATH, "(//button[contains(@class, 'btn_inventory')])[1]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    REMOVE_ITEM =(By.XPATH, "//button[@id='remove-sauce-labs-backpack']")

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage with the driver

    def add_first_item_to_cart(self):
        self.click_element(self.FIRST_ITEM_ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click_element(self.CART_ICON)

    def is_item_in_cart(self):
        return self.find_element(self.CART_BADGE).is_displayed()

    def remove_item_from_cart(self):
        self.click_element(self.REMOVE_ITEM)



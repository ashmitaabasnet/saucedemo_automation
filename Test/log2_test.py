import time
import logging
from selenium.webdriver.common.by import By
from Pages.product_page import ProductPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def test_add_to_cart(login):
    """Test adding an item to the cart after a successful login."""
    logging.info("Starting test: add item to cart.")
    product_page = ProductPage(login)

    # Add the first item to the cart
    product_page.add_first_item_to_cart()
    logging.info("First item added to the cart.")

    # Verify the item has been added by checking the cart badge
    if product_page.is_item_in_cart():
        logging.info("Item is present in the cart.")
    else:
        logging.error("Item was not added to the cart.")
    assert product_page.is_item_in_cart()

    time.sleep(3)


def test_go_to_cart(login):
    """Test navigating to the cart after adding an item."""
    logging.info("Starting test: go to cart.")
    product_page = ProductPage(login)

    # Add the first item to the cart
    product_page.add_first_item_to_cart()
    logging.info("First item added to the cart.")

    # Navigate to the cart
    product_page.go_to_cart()
    logging.info("Navigated to the cart.")

    # Verify that the cart page is displayed
    if login.find_element(By.CLASS_NAME, "cart_list").is_displayed():
        logging.info("Cart page is displayed.")
    else:
        logging.error("Cart page is not displayed.")
    assert login.find_element(By.CLASS_NAME, "cart_list").is_displayed()

    time.sleep(3)

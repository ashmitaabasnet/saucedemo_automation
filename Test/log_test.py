import time
import logging
from selenium.webdriver.common.by import By
from Pages.product_page import ProductPage

# Configure logging
logger = logging.getLogger() # Retrieves the root logger instance.
logger.setLevel(logging.INFO)  # Sets the logging level for the root logger to INFO

# Create handlers
console_handler = logging.StreamHandler()  # sends log message to console
file_handler = logging.FileHandler("info.log") # sends log message to a file

# Set the logging level for each handler
console_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def test_add_to_cart(login):
    """Test adding an item to the cart after a successful login."""
    logger.info("Starting test: add item to cart.")
    product_page = ProductPage(login)

    # Add the first item to the cart
    product_page.add_first_item_to_cart()
    logger.info("First item added to the cart.")

    # Verify the item has been added by checking the cart badge
    if product_page.is_item_in_cart():
        logger.info("Item is present in the cart.")
    else:
        logger.error("Item was not added to the cart.")
    assert product_page.is_item_in_cart()

    time.sleep(3)

def test_go_to_cart(login):
    """Test navigating to the cart after adding an item."""
    logger.info("Starting test: go to cart.")
    product_page = ProductPage(login)

    # Add the first item to the cart
    product_page.add_first_item_to_cart()
    logger.info("First item added to the cart.")

    # Navigate to the cart
    product_page.go_to_cart()
    logger.info("Navigated to the cart.")

    # Verify that the cart page is displayed
    if login.find_element(By.CLASS_NAME, "cart_list").is_displayed():
        logger.info("Cart page is displayed.")
    else:
        logger.error("Cart page is not displayed.")
    assert login.find_element(By.CLASS_NAME, "cart_list").is_displayed()

    time.sleep(3)


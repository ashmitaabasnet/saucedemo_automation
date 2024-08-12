import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.product_page import ProductPage

def test_add_to_cart(login):
    """Test adding an item to the cart after a successful login."""
    product_page = ProductPage(login)
    # Add first item to the cart
    product_page.add_first_item_to_cart()

    # Verify the item has been added by checking the cart page
    assert product_page.is_item_in_cart()
    time.sleep(3)

def test_go_to_cart(login):
    """Test navigating to the cart after adding an item."""
    # Add the first item to the cart
    product_page = ProductPage(login)
    product_page.add_first_item_to_cart()

    # Navigate to the cart
    product_page.go_to_cart()

    # Verify that the cart page is displayed
    assert login.find_element(By.CLASS_NAME, "cart_list").is_displayed()
    time.sleep(3)

def test_remove_item_from_cart(login):
    """Test removing an item from the cart and verifying the cart badge updates."""
    product_page = ProductPage(login)
    product_page.add_first_item_to_cart()

    # Navigate to the cart
    product_page.go_to_cart()
    #Remove Item from the cart
    product_page.remove_item_from_cart()




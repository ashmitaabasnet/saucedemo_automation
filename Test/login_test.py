
import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def driver():
    # Set up the WebDriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver  # Return the driver to the test function
    driver.quit()  # Close the browser after the test

def test_login_success(driver):
    """Test a successful login with valid credentials."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Verify that the login was successful by checking for an element on the home page
    assert driver.find_element(By.CLASS_NAME, "inventory_list").is_displayed()

def test_login_failure(driver):
    """Test a login with invalid credentials."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Verify that the login failed by checking for the error message
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.is_displayed()

def test_empty_fields(driver):
    """Test a login with empty credentials."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.is_displayed()

def test_login_empty_password(driver):
    """Test a login with empty password."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("standard_user")
    login_page.click_login()

    # Verify that the login failed by checking for the error message
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.is_displayed()

def test_login_empty_username(driver):
    """Test a login with empty username."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Verify that the login failed by checking for the error message
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert error_message.is_displayed()

def test_login_locked_out_user(driver):
    """Test login with a locked out user."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_username("locked_out_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    error_message = driver.find_element(By.CLASS_NAME, "error-message-container")
    assert "Sorry, this user has been locked out." in error_message.text

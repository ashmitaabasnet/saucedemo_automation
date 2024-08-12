from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Log in to the site
username_field = driver.find_element(By.ID, "user-name")
username_field.clear()
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password")
password_field.clear()
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait for the page to load
time.sleep(3)


# List of options to test with their corresponding values
options = [
    ("Name (A to Z)", "az"),
    ("Name (Z to A)", "za"),
    ("Price (low to high)", "lohi"),
    ("Price (high to low)", "hilo")
]


def select_and_verify_option(visible_text, value):
    # Re-locate the dropdown element
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_visible_text(visible_text)
    print(f"Selected filter: {visible_text}")
    # Wait for the page to update with the selected filter
    time.sleep(5)
    # Verify that the filter is applied correctly by checking the active option text
    active_option = driver.find_element(By.CSS_SELECTOR, "span.active_option[data-test='active-option']").text
    print(f"Current selection: {active_option}")
    assert active_option == visible_text, f"Expected {visible_text}, but got {active_option}"

# Apply each filter
for visible_text, value in options:
    select_and_verify_option(visible_text, value)

# Close the browser
driver.quit()

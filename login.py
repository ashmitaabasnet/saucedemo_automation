from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox() #Initializes a new Firefox browser session
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Find the username input field and enter the username
username_field = driver.find_element(By.ID, "user-name")
username_field.clear()
username_field.send_keys("standard_user")

# Find the password input field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.clear()
password_field.send_keys("secret_sauce")

# Find the login button and click it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(10)
# Close the browser
driver.quit()


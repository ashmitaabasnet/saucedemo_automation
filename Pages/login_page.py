from selenium.webdriver.common.by import By
from Utilities.base_page import BasePage

class LoginPage(BasePage):
# locators
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)  # Initialize BasePage with the driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.enter_text(self.username_field, username)

    def enter_password(self, password):
        self.enter_text(self.password_field, password)

    def click_login(self):
        self.click_element(self.login_button)



# class LoginPage:
#     #locators
#     username_field = (By.ID, "user-name")
#     password_field = (By.ID, "password")
#     login_button = (By.ID, "login-button")
#
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def open(self):
#         self.driver.get("https://www.saucedemo.com/")
#
#     def enter_username(self, username):
#         self.driver.find_element(self.username_field).send_keys(username)
#
#     def enter_password(self, password):
#         self.driver.find_element(self.password_field).send_keys(password)
#
#     def click_login(self):
#         self.driver.find_element(self.login_button).click()







from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from STP import settings

class LoginPage:

    # PARAMS

    STANDARD_USER = settings
    INVALID_USER = ...
    PASSWORD = ...

    # Page locators

    LOGIN_URL = ...
    USERNAME_FIELD = ...
    PASSWORD_FIELD = ...
    LOGIN_BUTTON = ...

    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return self.LOGIN_URL

    @property
    def username_field_element(self):
        return self.driver.find_element(*self.USERNAME_FIELD)

    @property
    def password_field_element(self):
        return self.driver.find_element(*self.PASSWORD_FIELD)

    @property
    def login_button_element(self):
        return self.browser.find_element(*self.LOGIN_BUTTON)

    
    # Page Actions
    @property
    def load_login_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def enter_username(self, username):
        self.username_field_element.send_keys(username)

    @property
    def enter_password(self):
        self.password_field_element().send_keys(self.PASSWORD)

    @property
    def click_login_button(self):
        self.login_button_element.click()

    @property
    def log_in_standard_user(self):
        self.load_login_page()
        self.enter_username('user')
        self.enter_password()
        self.click
    
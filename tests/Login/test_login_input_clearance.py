import pytest
from selenium.webdriver import Keys
from pages.login_page import LoginPage
from util.base import BaseTest
import time

class TestLogin(BaseTest):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.loginpage = LoginPage(self.driver)  # Common setup
        self.loginpage.load()  # Load the login page for every test

    @pytest.mark.login
    def test_clear_username(self):
        # Enter a username and clear it
        self.loginpage.enter_username("Ad")
        time.sleep(1)
        # Simulate backspacing all the letters typed
        username_element = self.driver.find_element(*self.loginpage.username_field)
        username_length = len("Ad")
        # Use backspace to remove all characters
        for _ in range(username_length):
            username_element.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        # Verify the error message is displayed again
        assert self.loginpage.is_username_required_error_displayed(), "Username required message not displayed"
        #Start typing again to check if error message disappears
        self.loginpage.enter_username("Admin")
        assert self.loginpage.is_username_error_message_not_visible(), "Error message should not be visible after typing."


    @pytest.mark.login
    def test_clear_password(self):
        self.loginpage.enter_password("Ad")
        time.sleep(1)
        # Simulate backspacing all the letters typed
        password_element = self.driver.find_element(*self.loginpage.password_field)
        password_length = len("Ad")
        # Use backspace to remove all characters
        for _ in range(password_length):
            password_element.send_keys(Keys.BACKSPACE)
        time.sleep(1)
        # Verify the error message is displayed again
        assert self.loginpage.is_password_required_error_displayed(), "Password required message not displayed"
        #Start typing again to check if error message disappears
        self.loginpage.enter_password("Admin")
        assert self.loginpage.is_password_error_message_not_visible(), "Error message should not be visible after typing."


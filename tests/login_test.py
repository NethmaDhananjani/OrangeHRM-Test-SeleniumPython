import pytest
import time  # Import the time module to add sleep delays
from pages.login_page import LoginPage
from util.base import BaseTest

class TestLogin(BaseTest):
    def test_login(self):
        self.keep_browser_open = True  # Set flag to keep the browser open
        self.loginpage = LoginPage(self.driver)

        # Load the login page
        self.loginpage.load()

        # Enter username
        self.loginpage.enter_username("Admin")

        # Enter password
        self.loginpage.enter_password("admin123")

        self.loginpage.click_login_button()
        time.sleep(2)  # Pause for 2 seconds 

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
from pages.login_page import LoginPage
from util.base import BaseTest

class TestSuccesfulLogin(BaseTest):
    def test_successful_login(self):
        self.keep_browser_open = True  # Set flag to keep the browser open
        self.loginpage = LoginPage(self.driver)

        # Step 1: Load the login page
        self.loginpage.load()

        # Step 2: Enter login credentials and log in
        self.loginpage.enter_username("Admin")
        self.loginpage.enter_password("admin123")
        self.loginpage.click_login_button()

        # Wait for the dashboard URL to load after login
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        ), "URL did not change to dashboard after successful login"

        # Optionally return the driver if you want to use it in another test
        return self.driver  # Return the driver if needed in other tests

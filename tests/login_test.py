from telnetlib import EC

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import LoginPage
from util.base import BaseTest

class TestLogin(BaseTest):
    def test_login(self):
        self.keep_browser_open = True  # Set flag to keep the browser open
        self.loginpage = LoginPage(self.driver)

        # Step 1: Load the login page
        self.loginpage.load()

        # Step 2: Enter login credentials
        self.loginpage.enter_username("Admin")
        self.loginpage.enter_password("admin123")

        # Step 3: Click the login button
        self.loginpage.click_login_button()
        time.sleep(2)

        # Step 4: Wait for the login to complete (or verify login)
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "dashboard"))
        # )


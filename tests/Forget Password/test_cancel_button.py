import pytest
from pages.login_page import LoginPage
from pages.forgetPassword_page import ForgetPasswordPage
from util.base_withoutbrowserclose import BaseTestBrowser
import time

class TestCancelFunctionality(BaseTestBrowser):
    def test_cancel_button(self):
        self.keep_browser_open = True
        self.loginpage = LoginPage(self.driver)
        self.forgetpasswordpage = ForgetPasswordPage(self.driver)

        # Step 1: Load the login page and navigate to Forgot Password page
        self.loginpage.load()
        self.loginpage.click_forgot_password()

        # Step 2: Click on 'Cancel' to navigate back to the login screen
        self.forgetpasswordpage.click_cancel_button()
        time.sleep(2)

        # Step 3: Verify navigation back to login page
        # assert self.loginpage.is_login_page(), "Should navigate back to the login page."

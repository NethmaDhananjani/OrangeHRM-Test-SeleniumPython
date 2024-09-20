from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

        self.forget_password_link = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
        self.linkedin_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[1]')
        self.facebook_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[2]')
        self.twitter_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[3]')
        self.youtube_icon = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/a[4]')

    def load(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enter_username(self, query):
        username_element = self.driver.find_element(*self.username_field)
        username_element.send_keys(query)

    def enter_password(self, pquery):
        password_element = self.driver.find_element(*self.password_field)
        password_element.send_keys(pquery)

    def click_login_button(self):
        login_button_element = self.driver.find_element(*self.login_button)
        login_button_element.click()

    def click_forgot_password(self):
        """Click the 'Forgot Password' link."""
        forgot_password_element = self.driver.find_element(*self.forget_password_link)
        forgot_password_element.click()

    def click_linkedin_icon(self):
        """Click the LinkedIn icon and switch to the new tab."""
        linkedin_element = self.driver.find_element(*self.linkedin_icon)
        linkedin_element.click()
        # Switch to the new tab
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])  # Switch to the newly opened LinkedIn tab

    def click_facebook_icon(self):
        """Click the Facebook icon and switch to the new tab."""
        facebook_element = self.driver.find_element(*self.facebook_icon)
        facebook_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def click_twitter_icon(self):
        """Click the Twitter icon and switch to the new tab."""
        twitter_element = self.driver.find_element(*self.twitter_icon)
        twitter_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def click_youtube_icon(self):
        """Click the YouTube icon and switch to the new tab."""
        youtube_element = self.driver.find_element(*self.youtube_icon)
        youtube_element.click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
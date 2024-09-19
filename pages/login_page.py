from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')

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
from asyncio import timeout

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NationalitiesPage:
    def __init__(self, driver):
        self.driver = driver
        self.nationalities_tab = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
        self.add_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button')
        self.edit_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[3]/div/button[2]')
        self.delete_button = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[3]/div/button[1]')
        self.individual_checkbox1 = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        self.individual_checkbox2 = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        self.individual_checkbox3 = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        self.individual_checkbox1 = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        self.overall_checkbox = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div[1]/div/label/span/i')
        self.record_count_label = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[2]/div')


    def click_nationalities_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.nationalities_tab)
        ).click()

    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()

    def click_edit_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.edit_button)
        ).click()

    def click_overall_checkbox(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.overall_checkbox)
        ).click()

    def click_delete_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()
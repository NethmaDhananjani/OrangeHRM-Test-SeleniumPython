from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BaseTestBrowser:
    @classmethod
    def setup_class(cls):
        """Setup method to initialize the browser before all tests in the class."""
        # Set Chrome options to load Google as the homepage
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")  # Start Chrome maximized
        chrome_options.add_argument("--disable-notifications")  # Disable notifications
        chrome_options.add_argument("--disable-infobars")  # Disable Chrome's infobar
        chrome_options.add_argument("homepage=https://www.google.com")  # Set Google as homepage
        chrome_options.add_argument("--no-first-run")  # Disable first-run experience

        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(10)

    @classmethod
    def teardown_class(cls):
        """Teardown method to clean up after all tests in the class."""
        cls.driver.quit()

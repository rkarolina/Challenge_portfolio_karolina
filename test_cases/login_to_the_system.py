import os
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

# TC001 - test case TC001 - login to the Scouts Panel
class TestLoginPage(unittest.TestCase):
    driver_service = None
    driver = None
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        # self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email(' ')
        user_login.type_in_password(' ')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()

    @classmethod
    def tearDown(self):
        self.driver.quit()

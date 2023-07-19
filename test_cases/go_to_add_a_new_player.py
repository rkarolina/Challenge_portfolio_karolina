import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import IMPLICITLY_WAIT, DRIVER_PATH

# TC003 - test case TC003 - add a new player
class TestAddPlayer(unittest.TestCase):
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

    def test_add_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check the title of page
        user_login.type_in_email('user01@getnada.com')  # type email
        user_login.type_in_password('Test-1234')  # type password
        user_login.click_sign_in_button()  # click on the button to sign in.

        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()  # check the title of dashboard page
        dashboard_page.click_add_player_button()  # click on the button aa player
        add_a_player_page = AddPlayer(self.driver)  # go to add player page
        add_a_player_page.title_of_page()
        add_a_player_page.type_in_playeremail('maciejmaciejtest@gmail.com')
        add_a_player_page.type_in_name('Maciej')
        add_a_player_page.type_in_surname('Maciejtest')
        add_a_player_page.type_in_age('01.01.1995')
        add_a_player_page.type_in_mainPosition('bramkarz')
        add_a_player_page.click_submit_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()

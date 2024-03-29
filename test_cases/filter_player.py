import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.dashboard import Dashboard
from pages.edit_players import EditPlayer
from pages.login_page import LoginPage
from pages.players import Players
from utils.settings import IMPLICITLY_WAIT, DRIVER_PATH
# TC004 - test case TC004 - filter player

class TestFilterPlayer(unittest.TestCase):
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

    def test_filter_player(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check the title of page
        user_login.type_in_email(' ')  # type email
        user_login.type_in_password(' ')  # type password
        user_login.click_sign_in_button()  # click on the button to sign in.

        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()  # check the title of dashboard page
        dashboard_page.click_players_button()  # click players button

        players_page = Players(self.driver)  # go to add player page
        players_page.title_of_page()  # check the title of add player page
        players_page.click_filter_button()
        players_page.type_in_name('Maciej')  # type player's first name
        players_page.type_in_surname('Bongos')  # type player's surname
        players_page.type_in_age_min('0')
        players_page.type_in_age_max('20')
        players_page.type_in_main_position('bramkarz')
        players_page.type_in_club('fc barcelona')
        players_page.type_in_rate_min('0')
        players_page.type_in_rate_max('5')
        time.sleep(2)
        players_page.click_close_filter()
        time.sleep(2)
        players_page.click_first_result()
        time.sleep(2)
        edit_players_page = EditPlayer(self.driver)
        filtered_player_name = edit_players_page.get_filtered_player_name()
        filtered_player_surname = edit_players_page.get_filtered_player_surname()
        assert filtered_player_name.get_attribute('value') == 'Maciej'
        assert filtered_player_surname.get_attribute('value') == 'Bongos'
    @classmethod
    def tearDown(self):
        self.driver.quit()

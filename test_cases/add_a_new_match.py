import os
import time
import unittest
from lib2to3.pgen2.driver import Driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.add_match import AddMatch
from pages.dashboard import Dashboard
from pages.edit_players import EditPlayer
from pages.login_page import LoginPage
from pages.matches import Matches
from pages.players import Players
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium import webdriver

# TC005 - test case TC005 - Add new match
class TestAddNewMatch(unittest.TestCase):
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
        # self.driver.set_script_timeout(300)

    def test_add_new_match(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check the title of page
        user_login.type_in_email('user01@getnada.com')  # type email
        user_login.type_in_password('Test-1234')  # type password
        user_login.click_sign_in_button()  # click on the button to sign in.

        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()  # check the title of dashboard page
        dashboard_page.click_players_button()  # click players button

        players_page = Players(self.driver)  # go to add player page
        players_page.title_of_page()  # check the title of add player page
        players_page.click_filter_button()
        # players_page.type_in_name('')  # type player's first name
        # players_page.type_in_surname('')  # type player's surname
        players_page.type_in_age_min('17')
        players_page.type_in_age_max('29')
        players_page.type_in_main_position('bramkarz')
        # players_page.type_in_club('')
        players_page.type_in_rate_min('0')
        players_page.type_in_rate_max('50')
        time.sleep(2)
        players_page.click_close_filter()
        time.sleep(2)
        players_page.click_first_result()
        time.sleep(2)

        # go to edit player form
        edit_players_page = EditPlayer(self.driver)  # go to add player page
        # edit_players_page.title_of_page()  # check the title of add player page
        edit_players_page.click_matches_button()
        time.sleep(2)
        # go to edit matches form
        matches_page = Matches(self.driver)  # go to add player page
        matches_page.title_of_page()  # check the title of add player page
        matches_page.click_on_add_match_button()
        time.sleep(2)

        # go to add match form
        add_match_page = AddMatch(self.driver)  # go to add player page
        add_match_page.title_of_page()  # check the title of add player page
        add_match_page.type_in_my_team('Cracovia')
        add_match_page.type_in_enemy_team('Legia Warszawa')
        add_match_page.type_in_my_team_score('3')
        add_match_page.type_in_enemy_team_score('2')
        add_match_page.type_in_match_date('11.07.2023')
        add_match_page.click_in_match_at_home()
        # add_match_page.click_in_match_out_home()
        add_match_page.type_in_tshirt('white')
        add_match_page.type_in_league('Ekstraklasa')
        add_match_page.type_in_time_played('120')
        add_match_page.type_in_number('11')
        add_match_page.type_in_web_match('yes')
        add_match_page.type_in_web_general('yes')
        add_match_page.type_in_rating('5')
        add_match_page.click_in_submit()
        time.sleep(2)
        # back to matches page
        matches_page = Matches(self.driver)  # go to add player page
        matches_page.title_of_page()  # check the title of add player page
        matches_page.click_back_to_main_page_button()
        time.sleep(2)
        # go to dashboard page to check last created match
        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()  # check the title of dashboard page
        last_added_match = dashboard_page.get_last_created_match()
        assert last_added_match.text == 'Cracovia - Legia Warszawa'.upper()
    @classmethod
    def tearDown(self):
        self.driver.quit()
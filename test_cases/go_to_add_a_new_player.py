import os
import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from pages.edit_players import EditPlayer
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
        dashboard_page.click_add_player_button()  # click on the button add player
        add_a_player_page = AddPlayer(self.driver)  # go to add player page
        add_a_player_page.title_of_page()  # check the title of add player page
        add_a_player_page.type_in_player_email('test_maciej@gmail.com')  # type player's email
        add_a_player_page.type_in_name('test')  # type player's first name
        add_a_player_page.type_in_surname('maciej')  # type player's surname
        add_a_player_page.type_in_phone('500111236')
        add_a_player_page.type_in_weight('70')
        add_a_player_page.type_in_height('169')
        add_a_player_page.type_in_age('01.01.1995')
        add_a_player_page.select_leg_dropdown('Left Leg')
        add_a_player_page.type_in_club('AC Milan')
        add_a_player_page.type_in_level('łatwy')
        add_a_player_page.type_in_mainPosition('bramkarz')
        add_a_player_page.type_in_secondposition('obrońca')

        add_a_player_page.select_district_dropdown('Lublin')
        add_a_player_page.type_in_achievements('mistrz Polski')
        add_a_player_page.click_addLanguage_button()
        add_a_player_page.type_in_languagesToProvide('ENG')
        # Part of TC005
        add_a_player_page.type_in_laczyNasPilka('maciejmaciejtest')
        add_a_player_page.type_in_ninetyMinutes('maciejmaciejtest2')
        add_a_player_page.type_in_facebookField('brak')
        add_a_player_page.click_addLinkToYoutube_button()
        add_a_player_page.type_in_youtubeField('youtube/maciejmaciejtest')
        add_a_player_page.click_submit_button()
        edit_page = EditPlayer(self.driver)  # go to edit player page
        edit_page.title_of_page()
        # compare last added player on dashboard page with my last added player
        edit_page.click_on_main_page_button()  # go to dashboard page to check last added player
        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()
        dashboard_page.click_last_created_player_button()
        time.sleep(4)
        # edit_page = EditPlayer(self.driver)  # go to edit player page
        # edit_page.title_of_page2()
    @classmethod
    def tearDown(self):
        self.driver.quit()

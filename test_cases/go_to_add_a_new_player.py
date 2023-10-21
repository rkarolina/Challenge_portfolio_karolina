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
        user_login.type_in_email(' ')  # type email
        user_login.type_in_password(' ')  # type password
        user_login.click_sign_in_button()  # click on the button to sign in.

        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()  # check the title of dashboard page
        dashboard_page.click_add_player_button()  # click on the button add player
        add_a_player_page = AddPlayer(self.driver)  # go to add player page
        add_a_player_page.title_of_page()  # check the title of add player page
        add_a_player_page.type_in_player_email('myemail@email.com')  # type player's email
        add_a_player_page.type_in_name('imie')  # type player's first name
        add_a_player_page.type_in_surname('nazwisko')  # type player's surname
        add_a_player_page.type_in_phone('500111236')
        add_a_player_page.type_in_weight('700')
        add_a_player_page.type_in_height('169')
        add_a_player_page.type_in_age('12.12.1999')
        add_a_player_page.select_leg_dropdown('Left leg')
        add_a_player_page.type_in_club('AC Milan')
        add_a_player_page.type_in_level('łatwy')
        add_a_player_page.type_in_main_position('bramkarz')
        add_a_player_page.type_in_secondposition('obrońca')
        add_a_player_page.select_district_dropdown('Lublin')
        add_a_player_page.type_in_achievements('mistrz Polski')
        add_a_player_page.click_addLanguage_button()
        add_a_player_page.type_in_languagesToProvide('ENG')
        add_a_player_page.type_in_laczyNasPilka('Elisabeth123!')
        add_a_player_page.type_in_ninetyMinutes('Elisabeth123!')
        add_a_player_page.type_in_facebookField('brak')
        add_a_player_page.click_addLinkToYoutube_button()
        add_a_player_page.type_in_youtubeField('youtube.com/Elisabeth123')
        add_a_player_page.click_submit_button()
        # add_a_player_page.click_clear_button()
        edit_page = EditPlayer(self.driver)  # go to edit player page
        edit_page.title_of_page()
        # compare last added player on dashboard page with my last added player
        edit_page.click_on_main_page_button()  # go to dashboard page to check last added player
        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()

        last_added_player = dashboard_page.get_last_created_player()
        assert last_added_player.text == 'imie nazwisko'.upper()
    @classmethod
    def tearDown(self):
        self.driver.quit()

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

# TC006 - test case TC006 - Edit existing Player
class TestEditPlayer(unittest.TestCase):
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
        dashboard_page.click_players_button()  # click on the button Gracze/Players
        players_page = Players(self.driver)  # go to add player page
        # players_page.title_of_page()  # check the title of add player page
        players_page.click_filter_button()
        players_page.type_in_name('J')  # type player's first name
        players_page.type_in_surname('Lopez')  # type player's surname
        players_page.click_close_filter()
        time.sleep(2)
        players_page.click_first_result()
        edit_players_page = EditPlayer(self.driver)  # go to add player page
        # edit_players_page.title_of_page()
        edit_players_page.type_in_player_email('aniakwiatek@gmail.com')
        edit_players_page.type_in_player_phone('78934569888')
        edit_players_page.type_in_player_weight(40)
        edit_players_page.type_in_player_height(20)
        edit_players_page.type_in_player_age('12.12.2012')
        edit_players_page.type_in_player_club('Cracovia')
        edit_players_page.type_in_player_level('intermediate')
        edit_players_page.type_in_player_main_position('napastnik')
        edit_players_page.type_in_player_second_position('obrońca')
        edit_players_page.type_in_achievements('new achievement')
        edit_players_page.click_addLanguage_button()
        edit_players_page.type_in_languagesToProvide('PL')
        time.sleep(5)
        edit_players_page.type_in_laczyNasPilka('laczyNasPilka.link')
        edit_players_page.type_in_ninetyMinutes('nope')
        edit_players_page.type_in_facebook_field('facebook/new')
        edit_players_page.click_addLinkToYoutube_button()
        edit_players_page.type_in_youtube_field('new youtube field')
        edit_players_page.click_submit_button()
        # back to main page
        edit_players_page.click_on_main_page_button()
        time.sleep(2)
        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        dashboard_page.title_of_page()

        last_updated_player = dashboard_page.get_last_updated_player()
        assert last_updated_player.text == 'J Lopez'.upper()

    @classmethod
    def tearDown(self):
        self.driver.quit()
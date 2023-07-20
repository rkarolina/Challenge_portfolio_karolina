import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from pages.edit_players import EditPlayer
from pages.login_page import LoginPage
from utils.settings import IMPLICITLY_WAIT, DRIVER_PATH

# TC004 - test case TC004 - Edit existing Player
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
    def test_add_new_match(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()  # check the title of page
        user_login.type_in_email('user01@getnada.com')  # type email
        user_login.type_in_password('Test-1234')  # type password
        user_login.click_sign_in_button()  # click on the button to sign in.

        dashboard_page = Dashboard(self.driver)  # go to dashboard page
        # dashboard_page.title_of_page()  # check the title of dashboard page
        dashboard_page.click_players_button()  # click on the button Gracze/Players
        edit_players_page = EditPlayer(self.driver)  # go to add player page
        # edit_players_page.title_of_page()
        edit_players_page.type_in_search('maciejmaciejtest@gmail.com')
        edit_players_page.click_first_result()
        add_a_player_page = AddPlayer(self.driver)
        edit_players_page.type_in_editfacebookField('test')
        add_a_player_page.type_in_laczyNasPilka('XD')
        add_a_player_page.type_in_ninetyMinutes('XD')
        # add_a_player_page.type_in_facebookField('brak')
        add_a_player_page.click_addLinkToYoutube_button()
        add_a_player_page.type_in_youtubeField('XD')
        add_a_player_page.click_submit_button()
        time.sleep(8)

    @classmethod
    def tearDown(self):
        self.driver.quit()
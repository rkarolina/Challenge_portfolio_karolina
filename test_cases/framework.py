import os
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))
        self.driver.get('https://scouts.test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")

class TestMediumPage(unittest.TestCase):

        @classmethod
        def setUp(self):
            os.chmod(DRIVER_PATH, 755)
            self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))
            self.driver.get('https://medium.com/')
            self.driver.fullscreen_window()
            self.driver.implicitly_wait(IMPLICITLY_WAIT)

        def test_check_title(self):
            actual_title = self.get_page_title('https://medium.com/')
            expected_title = 'Medium – Where good ideas find you.'
            assert actual_title == expected_title
        def get_page_title(self, url):
            self.driver.get(url)
            return self.driver.title

        @classmethod
        def tearDown(self):
            self.driver.quit()

    # Element of the first task: Try to search the Internet yourself how to get rid of the error:
    # "DeprecationWarning: executable_path has been deprecated, please pass in a Service object"
class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(service=Service(DRIVER_PATH))
        self.driver.get('https://scouts.futbolkolektyw.pl')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_print_nice_words(self):
        print("WELL DONE!!!!!!!!!")
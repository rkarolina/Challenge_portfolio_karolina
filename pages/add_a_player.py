import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_button_xpath = "//a[contains(@href, '/en/players/add')]"
    addPlayer_url = ('https://scouts-test.futbolkolektyw.pl/players/add')
    expected_title = "Add player"

    def click_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        time.sleep(4)
        assert self.get_page_title(self.addPlayer_url) == self.expected_title
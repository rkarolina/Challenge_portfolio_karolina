from pages.base_page import BasePage


class EditPlayer(BasePage):
    addPlayer_url = ('https://scouts-test.futbolkolektyw.pl/en/players')
    players_xpatch = "//ul[1]/div[2]/div[2]/span"
    search_xpatch = "//div/div[1]/div[2]/input"

    def type_in_search(self, search):
        self.wait_for_element_to_be_clickable(self.search_xpatch)
        self.field_send_keys(self.search_xpatch, search)

    def click_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_xpatch)
        self.click_on_the_element(self.players_xpatch)
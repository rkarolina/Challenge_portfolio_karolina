import time

from pages.base_page import BasePage

class Dashboard(BasePage):
    expected_title = "Scouts panel"
    dashboard_url = "https://scouts-test.futbolkolektyw.pl/en"
    MainPage_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//ul[1]/div[2]/div[2]/span"
    polski_button_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    add_player_button_xpath = "//a[contains(@href, '/en/players/add')]"
    dev_team_contact_button_xpath = "//a[contains(@href, '://')]"
    last_created_player_text_xpath = "//*[text()='Last created player']"
    last_created_player_value_xpath = "//div[3]/div/div/a[1]/button/span[1]"
    last_created_player_button_xpath = "//div[3]/div/div/a[1]/button/span[2]"
    last_updated_player_name_xpath = "//*[text()='Last updated player']"
    last_updated_player_button_xpath = "//div/div/a[2]/button/span[1]"
    last_created_match_name_xpath = "//*[text()='Last created match']"
    last_created_match_button_xpath = "//a[3]/button/span[1]"
    last_updated_match_name_xpath = "//*[text()='Last updated match']"
    last_updated_match_button_xpath = "//a[4]/button/span[1]"
    last_updated_report_name_xpath = "//*[text()='Last updated report']"
    last_updated_report_button_xpath = "//div/div/a[5]/button/span[1] "

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.players_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player_button(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        self.click_on_the_element(self.add_player_button_xpath)

    def click_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_button_xpath)
        self.click_on_the_element(self.players_button_xpath)
    # to compare with results of other test cases
    def click_last_created_player_button(self):
        self.wait_for_element_to_be_clickable(self.last_created_player_value_xpath)
        self.click_on_the_element(self.last_created_player_value_xpath)

    def click_last_updated_player_button(self):
        self.wait_for_element_to_be_clickable(self.last_updated_player_button_xpath)
        self.click_on_the_element(self.last_updated_player_button_xpath)

    def click_last_updated_match_button(self):
        self.wait_for_element_to_be_clickable(self.last_updated_match_button_xpath)
        self.click_on_the_element(self.last_updated_match_button_xpath)

    def click_last_updated_report(self):
        self.wait_for_element_to_be_clickable(self.last_updated_report_button_xpath)
        self.click_on_the_element(self.last_updated_report_button_xpath)

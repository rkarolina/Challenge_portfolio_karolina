from pages.base_page import BasePage

class Matches(BasePage):
    players_url = ".+(?=\/matches$).+"
    expected_title = "Matches player"
    main_page_xpath = "//*[text()='Main page' or text()='Strona główna']"
    players_xpath = "//*[text()='Players' or text()='Gracze']"
    back_to_player_xpath = "//ul[2]/div[1]/div[2]/span"
    matches_xpath = "//*[text()='Matches' or text()='Mecze']"
    reports_xpath = "//*[text()='Reports' or text()='Raporty']"
    polski_english_xpath = "//*[text()='Polski' or text()='English']"
    sign_out_xpath = "//*[text()='Sign out' or text()='Wyloguj']"
    add_match_xpath = "//*[text()='Add match' or text()='Dodaj mecz']"

    def click_on_add_match_button(self):
        self.wait_for_element_to_be_clickable(self.add_match_xpath)
        self.click_on_the_element(self.add_match_xpath)

    def click_back_to_main_page_button(self):
        self.wait_for_element_to_be_clickable(self.main_page_xpath)
        self.click_on_the_element(self.main_page_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.back_to_player_xpath)
        assert self.driver.title.__contains__(self.expected_title)

from selenium.webdriver import Keys

from pages.base_page import BasePage


class Players(BasePage):
    players_url = "https://scouts-test.futbolkolektyw.pl/en/players"
    expected_title = "Players"
    download_csv_button_xpath = "//*[@data-testid='Download CSV-iconButton']"
    filter_table_button_xpath = "//*[@data-testid='Filter Table-iconButton']"
    firstPlayer_xpath = "//*[@id='MUIDataTableBodyRow-0']"
    search_input_xpath = "//*[@class='MuiInputBase-input jss41']"
    name_xpath = "//div[2]/div[1]/div/div/div/input"
    surname_xpath = "//div[2]/div[3]/div/div[2]/div[2]/div/div/div/input"
    age_min_xpath = "//div[2]/div[3]/div/div/div/div[1]/div/input"
    age_max_xpath = "//div[3]/div/div[2]/div[3]/div/div/div/div[2]/div/input"
    main_position_xpath = "//div[4]/div/div/div/input"
    club_xpath = "//div/div[2]/div[5]/div/div/div/input"
    rate_min_xpath = "//div[2]/div[6]/div/div/div/div[1]/div/input"
    rate_max_xpath = "//div[6]/div/div/div/div[2]/div/input"
    reset_button_xpath = "//div[1]/div[1]/button/span[1]"
    close_filter_xpath = "/html/body/div[2]/div[3]/button"

    def type_in_search(self, search):
        self.wait_for_element_to_be_clickable(self.search_input_xpath)
        self.field_send_keys(self.search_input_xpath, search)
        self.field_send_keys(self.search_input_xpath, Keys.ENTER)

    def click_download_csv_button(self):
        self.wait_for_element_to_be_clickable(self.download_csv_button_xpath)
        self.click_on_the_element(self.download_csv_button_xpath)

    def click_filter_button(self):
        self.wait_for_element_to_be_clickable(self.filter_table_button_xpath)
        self.click_on_the_element(self.filter_table_button_xpath)

    def type_in_name(self, name):
        self.wait_for_element_to_be_clickable(self.name_xpath)
        self.field_send_keys(self.name_xpath, name)

    def type_in_surname(self, surname):
        self.wait_for_element_to_be_clickable(self.surname_xpath)
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_age_min(self, age_min):
        self.wait_for_element_to_be_clickable(self.age_min_xpath)
        self.field_send_keys(self.age_min_xpath, age_min)

    def type_in_age_max(self, age_max):
        self.wait_for_element_to_be_clickable(self.age_max_xpath)
        self.field_send_keys(self.age_max_xpath, age_max)

    def type_in_club(self, club):
        self.wait_for_element_to_be_clickable(self.club_xpath)
        self.field_send_keys(self.club_xpath, club)

    def type_in_main_position(self, main_position):
        self.wait_for_element_to_be_clickable(self.main_position_xpath)
        self.field_send_keys(self.main_position_xpath, main_position)

    def type_in_rate_min(self, rate_min):
        self.wait_for_element_to_be_clickable(self.rate_min_xpath)
        self.field_send_keys(self.rate_min_xpath, rate_min)

    def type_in_rate_max(self, rate_max):
        self.wait_for_element_to_be_clickable(self.rate_max_xpath)
        self.field_send_keys(self.rate_max_xpath, rate_max)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.firstPlayer_xpath)
        assert self.driver.title.__contains__(self.expected_title)

    def click_close_filter(self):
        self.wait_for_element_to_be_clickable(self.close_filter_xpath)
        self.click_on_the_element(self.close_filter_xpath)

    def click_first_result(self):
        self.wait_for_element_to_be_clickable(self.firstPlayer_xpath)
        self.click_on_the_element(self.firstPlayer_xpath)

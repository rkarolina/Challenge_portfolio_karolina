from pages.base_page import BasePage


class Players(BasePage):
    Players_url = "https://scouts-test.futbolkolektyw.pl/en/players"
    expected_title = "Players"
    download_csv_button_xpath = "//*[@data-testid='Download CSV-iconButton']"

    def click_download_csv_button(self):
        self.wait_for_element_to_be_clickable(self.download_csv_button_xpath)
        self.click_on_the_element(self.download_csv_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.download_csv_button_xpath)
        assert self.driver.title.__contains__(self.expected_title)

from pages.base_page import BasePage


class Players(BasePage):
    Players_url = ('https://scouts.futbolkolektyw.pl/en/players')
    # expected_title = "Players (4063) page 1" - number of players is changing...
    download_csv_button_xpath = "//*[@data-testid='Download CSV-iconButton']"

    def click_download_csv_button(self):
        self.wait_for_element_to_be_clickable(self.download_csv_button_xpath)
        self.click_on_the_element(self.download_csv_button_xpath)

    # def title_of_page(self):
    #     assert self.get_page_title(self.Players_url) == self.expected_title

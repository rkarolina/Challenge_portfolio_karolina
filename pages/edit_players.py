from selenium.webdriver import Keys

from pages.base_page import BasePage


class EditPlayer(BasePage):
    addPlayer_url = "https://scouts.futbolkolektyw.pl/en/players"
    players_xpath = "//ul[1]/div[2]/div[2]/span"
    search_xpath = "//div/div[1]/div[2]/input"
    firstPlayer_xpath = "//*[@id='MUIDataTableBodyRow-0']"
    editFacebookField_xpath = "//input[@name='webFB']"
    # expected_title = ' '
    def type_in_search(self, search):
        self.wait_for_element_to_be_clickable(self.search_xpath)
        self.field_send_keys(self.search_xpath, search)
        self.field_send_keys(self.search_xpath, Keys.ENTER) #clicks enter
    def type_in_editfacebookField(self, editfacebookField):
        self.wait_for_element_to_be_clickable(self.editFacebookField_xpath)
        editfacebookField.sendKeys(Keys.BACK_SPACE)
        self.field_send_keys(self.editFacebookField_xpath, editfacebookField)
    def click_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_xpath)
        self.click_on_the_element(self.players_xpath)

    def click_first_result(self):
        self.wait_for_element_to_be_clickable(self.firstPlayer_xpath)
        self.click_on_the_element(self.firstPlayer_xpath)
    # def title_of_page(self):
    #     self.wait_for_element_to_be_clickable(self.firstPlayer_xpath)
    #     assert self.get_page_title(self.addPlayer_url) == self.expected_title
import time

from selenium.webdriver import Keys
from pages.base_page import BasePage
from pages.add_a_player import AddPlayer


class EditPlayer(BasePage):
    # editPlayer_url = ".+(?=\/edit$).+"
    main_page_xpath = "//*[text()='Main page']"
    players_xpath = "//ul[1]/div[2]/div[2]/span"
    search_xpath = "//div/div[1]/div[2]/input"
    redirect_to_edit_page = "// *[text() = 'Redirect to edit page']"
    my_current_player_button_xpath = "//ul[2]/div[1]/div[2]/span"
    editFacebookField_xpath = "//input[@name='webFB']"
    expected_title = "Edit player"
    firstPlayer_xpath = "//*[@id='MUIDataTableBodyRow-0']"

    def type_in_search(self, search):
        self.wait_for_element_to_be_clickable(self.search_xpath)
        self.field_send_keys(self.search_xpath, search)
        self.field_send_keys(self.search_xpath, Keys.ENTER)

    def type_in_editfacebookField(self, editfacebookField):
        self.wait_for_element_to_be_clickable(self.editFacebookField_xpath)
        editfacebookField.sendKeys(Keys.BACK_SPACE)
        self.field_send_keys(self.editFacebookField_xpath, editfacebookField)

    def click_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_xpath)
        self.click_on_the_element(self.players_xpath)

    def click_on_main_page_button(self):
        self.wait_for_element_to_be_clickable(self.main_page_xpath)
        self.click_on_the_element(self.main_page_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.redirect_to_edit_page)
        assert self.driver.title.__contains__(self.expected_title)
        # expected title which contains only the same words
        print(self.expected_title, self.driver.title)
        time.sleep(4)
        # my current player edit page title

    def click_first_result(self):
        self.wait_for_element_to_be_clickable(self.firstPlayer_xpath)
        self.click_on_the_element(self.firstPlayer_xpath)

    # def title_of_page2(self):
    #     self.wait_for_element_to_be_clickable(self.my_current_player_button_xpath)
    #     assert self.driver.title.__contains__(self.expected_title)
    #     print(self.expected_title, self.driver.title)
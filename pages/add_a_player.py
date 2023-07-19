import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_button_xpath = "//a[contains(@href, '/en/players/add')]"
    addPlayer_url = ('https://scouts-test.futbolkolektyw.pl/players/add')
    expected_title = "Add player"
    # selectors
    email_xpatch = "//input[@name='email']"
    name_xpatch = "//input[@name='name']"
    surname_xpatch = "//input[@name='surname']"
    phone_xpatch = "//input[@name='phone']"
    weight_xpatch = "//input[@name='weight']"
    height_xpatch = "//input[@name='height']"
    age_xpatch = "//input[@name='age']"
    leg_xpatch = "//*[@id='mui-component-select-leg']"
    club_xpatch = "//input[@name='club']"
    level_xpatch = "//input[@name='level']"
    mainPosition_xpatch = "//input[@name='mainPosition']"
    secondPosition_xpatch = "//input[@name='secondPosition']"
    district_xpatch = "//*[@id='mui-component-select-district']"
    achievements_xpatch = "//input[@name='achievements']"
    addLanguage_xpatch = "//div[15]/button/span[1]"
    languagesToProvide_xpatch = "//div[15]/div/div/div/input"
    removeLanguage_xpatch = "//*[@aria-label='Remove language']"
    laczyNasPilka_xpatch = "//input[@name='webLaczy']"
    ninetyMinutes_xpatch = "//input[@name='web90']"
    facebookField_xpatch = "//input[@name='webFB']"
    addLinkToYoutube_xpatch = "//*[@aria-label='Add link to Youtube']"
    youtubeField_xpatch = "//div[19]/div/div/div/input"
    removeLinkToYoutube_xpatch = "//div[2]/div/div[19]/div/button"
    submitAddPlayerbutton_xpatch = "//div[3]/button[1]/span[1]"
    clearAddPlayerbutton_xpatch = "//div[3]/button[2]/span[1]"

    def type_in_playeremail(self, playeremail):
        self.wait_for_element_to_be_clickable(self.email_xpatch)
        self.field_send_keys(self.email_xpatch, playeremail)
    def type_in_name(self, name):
        self.wait_for_element_to_be_clickable(self.name_xpatch)
        self.field_send_keys(self.name_xpatch, name)
    def type_in_surname(self, surname):
        self.wait_for_element_to_be_clickable(self.surname_xpatch)
        self.field_send_keys(self.surname_xpatch, surname)
    def type_in_age(self, age):
        self.wait_for_element_to_be_clickable(self.age_xpatch)
        self.field_send_keys(self.age_xpatch, age)

    def type_in_mainPosition(self, mainPosition):
        self.wait_for_element_to_be_clickable(self.mainPosition_xpatch)
        self.field_send_keys(self.mainPosition_xpatch, mainPosition)

    def click_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submitAddPlayerbutton_xpatch)
        self.click_on_the_element(self.submitAddPlayerbutton_xpatch)
    def click_add_player_button(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        self.click_on_the_element(self.add_player_button_xpath)

    def title_of_page(self):
        assert self.get_page_title(self.addPlayer_url) == self.expected_title
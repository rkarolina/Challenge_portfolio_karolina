
from pages.base_page import BasePage

class AddPlayer(BasePage):
    add_player_button_xpath = "//a[contains(@href, '/en/players/add')]"
    addPlayer_url = "https://scouts.futbolkolektyw.pl/players/add"
    expected_title = "Add player"
    # selectors
    email_xpath = "//input[@name='email']"
    name_xpath = "//input[@name='name']"
    surname_xpath = "//input[@name='surname']"
    phone_xpath = "//input[@name='phone']"
    weight_xpath = "//input[@name='weight']"
    height_xpath = "//input[@name='height']"
    age_xpath = "//input[@name='age']"
    # TODO.. leg XPATH
    leg_xpath = "//*[@id='mui-component-select-leg']"
    club_xpath = "//input[@name='club']"
    level_xpath = "//input[@name='level']"
    mainPosition_xpath = "//input[@name='mainPosition']"
    secondPosition_xpath = "//input[@name='secondPosition']"
    district_xpath = "//*[@id='mui-component-select-district']"
    achievements_xpath = "//input[@name='achievements']"
    addLanguage_xpath = "//div[15]/button/span[1]"
    languagesToProvide_xpath = "//div[15]/div/div/div/input"
    removeLanguage_xpath = "//*[@aria-label='Remove language']"
    laczyNasPilka_xpath = "//input[@name='webLaczy']"
    ninetyMinutes_xpath = "//input[@name='web90']"
    facebookField_xpath = "//input[@name='webFB']"
    addLinkToYoutube_xpath = "//*[@aria-label='Add link to Youtube']"
    youtubeField_xpath = "//div[19]/div/div/div/input"
    removeLinkToYoutube_xpath = "//div[2]/div/div[19]/div/button"
    submit_xpath = "//*[@type='submit']"
    clear_xpath = "//*[text()='Clear']"

    def type_in_playeremail(self, playeremail):
        self.wait_for_element_to_be_clickable(self.email_xpath)
        self.field_send_keys(self.email_xpath, playeremail)
    def type_in_name(self, name):
        self.wait_for_element_to_be_clickable(self.name_xpath)
        self.field_send_keys(self.name_xpath, name)
    def type_in_surname(self, surname):
        self.wait_for_element_to_be_clickable(self.surname_xpath)
        self.field_send_keys(self.surname_xpath, surname)
    def type_in_age(self, age):
        self.wait_for_element_to_be_clickable(self.age_xpath)
        self.field_send_keys(self.age_xpath, age)
    # TODO change name of the argument
    def type_in_mainPosition(self, mainPosition):
        self.wait_for_element_to_be_clickable(self.mainPosition_xpath)
        self.field_send_keys(self.mainPosition_xpath, mainPosition)

    # optional for Scouts Panel form
    def type_in_phone(self, phone):
        self.wait_for_element_to_be_clickable(self.phone_xpath)
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_weight(self, weight):
        self.wait_for_element_to_be_clickable(self.weight_xpath)
        self.field_send_keys(self.weight_xpath, weight)

    def type_in_height(self, height):
        self.wait_for_element_to_be_clickable(self.height_xpath)
        self.field_send_keys(self.height_xpath, height)

    def type_in_club(self, club):
        self.wait_for_element_to_be_clickable(self. club_xpath)
        self.field_send_keys(self.club_xpath, club)
    def type_in_level(self, level):
        self.wait_for_element_to_be_clickable(self.level_xpath)
        self.field_send_keys(self.level_xpath, level)
    def type_in_secondposition(self, secondposition):
        self.wait_for_element_to_be_clickable(self.secondPosition_xpath)
        self.field_send_keys(self.secondPosition_xpath, secondposition)
    def type_in_disctrict(self, district):
        self.wait_for_element_to_be_clickable(self.district_xpath)
        self.field_send_keys(self.district_xpath, district)
    def type_in_achievements(self, achievements):
        self.wait_for_element_to_be_clickable(self.achievements_xpath)
        self.field_send_keys(self.achievements_xpath, achievements)
    def click_addLanguage_button(self):
        self.wait_for_element_to_be_clickable(self.addLanguage_xpath)
        self.click_on_the_element(self.addLanguage_xpath)
    def type_in_languagesToProvide(self, languagesToProvide):
        self.wait_for_element_to_be_clickable(self.languagesToProvide_xpath)
        self.field_send_keys(self.languagesToProvide_xpath, languagesToProvide)
    def click_removeLanguage_button(self):
        self.wait_for_element_to_be_clickable(self.removeLanguage_xpath)
        self.click_on_the_element(self.removeLanguage_xpath)
    def type_in_laczyNasPilka(self, laczyNasPilka):
        self.wait_for_element_to_be_clickable(self.laczyNasPilka_xpath)
        self.field_send_keys(self.laczyNasPilka_xpath, laczyNasPilka)
    def type_in_ninetyMinutes(self, ninetyMinutes):
        self.wait_for_element_to_be_clickable(self.ninetyMinutes_xpath)
        self.field_send_keys(self.ninetyMinutes_xpath, ninetyMinutes)
    def type_in_facebookField(self, facebookField):
        self.wait_for_element_to_be_clickable(self.facebookField_xpath)
        self.field_send_keys(self.facebookField_xpath, facebookField)
    def click_addLinkToYoutube_button(self):
        self.wait_for_element_to_be_clickable(self.addLinkToYoutube_xpath)
        self.click_on_the_element(self.addLinkToYoutube_xpath)
    def type_in_youtubeField(self, youtubeField):
        self.wait_for_element_to_be_clickable(self.youtubeField_xpath)
        self.field_send_keys(self.youtubeField_xpath, youtubeField)
    def click_removeLinkToYoutube_button(self):
        self.wait_for_element_to_be_clickable(self.removeLinkToYoutube_xpath)
        self.click_on_the_element(self.removeLinkToYoutube_xpath)
    def click_clear_button(self):
        self.wait_for_element_to_be_clickable(self.clear_xpath)
        self.click_on_the_element(self.clear_xpath)
    def click_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_xpath)
        self.click_on_the_element(self.submit_xpath)
    def click_add_player_button(self):
        self.wait_for_element_to_be_clickable(self.add_player_button_xpath)
        self.click_on_the_element(self.add_player_button_xpath)
    def click_leg_dropdown(self):
        # leg = Select(driver.find_element_by_id('mui-component-select-leg)')
        self.wait_for_element_to_be_clickable(self.leg_xpath)
        self.click_on_the_element(self.leg_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.email_xpath)
        assert self.get_page_title(self.addPlayer_url) == self.expected_title
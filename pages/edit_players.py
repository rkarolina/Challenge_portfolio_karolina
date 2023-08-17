import time

from pages.base_page import BasePage
from pages.add_a_player import AddPlayer
from selenium.webdriver.common.keys import Keys

class EditPlayer(BasePage):
    # editPlayer_url = ".+(?=\/edit$).+"
    main_page_xpath = "//*[text()='Main page' or text()='Strona główna']"
    players_xpath = "//*[text()='Players' or text()='Gracze']"
    matches_xpath = "//*[text()='Matches' or text()='Mecze']"
    reports_xpath = "//*[text()='Reports' or text()='Raporty']"
    polski_english_xpath = "//*[text()='Polski' or text()='English']"
    sign_out_xpath = "//*[text()='Sign out' or text()='Wyloguj']"
    redirect_to_edit_page = "// *[text() = 'Redirect to edit page']"
    my_current_player_button_xpath = "//ul[2]/div[1]/div[2]/span"
    expected_title = "Edit player"

    email_xpath = "//input[@name='email']"
    name_xpath = "//input[@name='name']"
    surname_xpath = "//input[@name='surname']"
    phone_xpath = "//input[@name='phone']"
    weight_xpath = "//input[@name='weight']"
    height_xpath = "//input[@name='height']"
    age_xpath = "//input[@name='age']"
    leg_xpath = "//*[@id='mui-component-select-leg']"
    leg_menu_xpath = "//*[@class='MuiList-root MuiMenu-list MuiList-padding']"
    # right leg option in dropdown menu
    right_leg_xpath = "//*[contains(@data-value, 'right')]"
    # left leg option in dropdown menu
    left_leg_xpath = "//*[contains(@data-value, 'left')]"
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

    def get_filtered_player_name(self):
        return self.wait_for_element_to_be_clickable(self.name_xpath)

    def get_filtered_player_surname(self):
        return self.wait_for_element_to_be_clickable(self.surname_xpath)

    def type_in_player_email(self, email):
        self.wait_for_element_to_be_clickable(self.email_xpath)
        # clear previous value in the field
        self.field_send_keys(self.email_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.email_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.email_xpath, email)

    def type_in_player_name(self, name):
        self.wait_for_element_to_be_clickable(self.name_xpath)
        # clear previous value in the field
        self.field_send_keys(self.name_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.name_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.name_xpath, name)

    def type_in_player_surname(self, surname):
        self.wait_for_element_to_be_clickable(self.surname_xpath)
        # clear previous value in the field
        self.field_send_keys(self.surname_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.surname_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.surname_xpath, surname)

    def type_in_player_phone(self, phone):
        self.wait_for_element_to_be_clickable(self.phone_xpath)
        # clear previous value in the field
        self.field_send_keys(self.phone_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.phone_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.phone_xpath, phone)

    def type_in_player_weight(self, weight):
        self.wait_for_element_to_be_clickable(self.weight_xpath)
        # clear previous value in the field
        self.field_send_keys(self.weight_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.weight_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.weight_xpath, weight)

    def type_in_player_height(self, height):
        self.wait_for_element_to_be_clickable(self.height_xpath)
        # clear previous value in the field
        self.field_send_keys(self.height_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.height_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.height_xpath, height)

    def type_in_player_age(self, age):
        self.wait_for_element_to_be_clickable(self.age_xpath)
        # clear previous value in the field
        self.field_send_keys(self.age_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.age_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.age_xpath, age)
    # TODO leg right / left

    def type_in_player_club(self, club):
        self.wait_for_element_to_be_clickable(self.club_xpath)
        # clear previous value in the field
        self.field_send_keys(self.club_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.club_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.club_xpath, club)

    def type_in_player_level(self, level):
        self.wait_for_element_to_be_clickable(self.level_xpath)
        # clear previous value in the field
        self.field_send_keys(self.level_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.level_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.level_xpath, level)

    def type_in_player_main_position(self, mainPosition):
        self.wait_for_element_to_be_clickable(self.mainPosition_xpath)
        # clear previous value in the field
        self.field_send_keys(self.mainPosition_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.mainPosition_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.mainPosition_xpath, mainPosition)

    def type_in_player_second_position(self, secondPosition):
        self.wait_for_element_to_be_clickable(self.secondPosition_xpath)
        # clear previous value in the field
        self.field_send_keys(self.secondPosition_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.secondPosition_xpath, Keys.DELETE)
        # add new value to the field
        self.field_send_keys(self.secondPosition_xpath, secondPosition)
    def type_in_achievements(self, achievements):
        self.wait_for_element_to_be_clickable(self.achievements_xpath)
        self.field_send_keys(self.level_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.level_xpath, Keys.DELETE)
        self.field_send_keys(self.achievements_xpath, achievements)
    def click_addLanguage_button(self):
        self.wait_for_element_to_be_clickable(self.addLanguage_xpath)
        self.click_on_the_element(self.addLanguage_xpath)
    def type_in_languagesToProvide(self, languagesToProvide):
        self.wait_for_element_to_be_clickable(self.languagesToProvide_xpath)
        self.field_send_keys(self.level_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.level_xpath, Keys.DELETE)
        self.field_send_keys(self.languagesToProvide_xpath, languagesToProvide)
    def click_removeLanguage_button(self):
        self.wait_for_element_to_be_clickable(self.removeLanguage_xpath)
        self.click_on_the_element(self.removeLanguage_xpath)
    def type_in_laczyNasPilka(self, laczyNasPilka):
        self.wait_for_element_to_be_clickable(self.laczyNasPilka_xpath)
        self.field_send_keys(self.level_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.level_xpath, Keys.DELETE)
        self.wait_for_element_to_be_clickable(self.laczyNasPilka_xpath)
        self.field_send_keys(self.laczyNasPilka_xpath, laczyNasPilka)
    def type_in_ninetyMinutes(self, ninetyMinutes):
        self.wait_for_element_to_be_clickable(self.ninetyMinutes_xpath)
        self.field_send_keys(self.level_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.level_xpath, Keys.DELETE)
        self.wait_for_element_to_be_clickable(self.laczyNasPilka_xpath)
        self.field_send_keys(self.ninetyMinutes_xpath, ninetyMinutes)
    def type_in_facebook_field(self, facebook_field):
        self.wait_for_element_to_be_clickable(self.facebookField_xpath)
        self.field_send_keys(self.level_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.level_xpath, Keys.DELETE)
        self.wait_for_element_to_be_clickable(self.facebookField_xpath)
        self.field_send_keys(self.facebookField_xpath, facebook_field)
    def click_addLinkToYoutube_button(self):
        self.wait_for_element_to_be_clickable(self.addLinkToYoutube_xpath)
        self.click_on_the_element(self.addLinkToYoutube_xpath)

    def type_in_youtube_field(self, youtube_field):
        self.wait_for_element_to_be_clickable(self.youtubeField_xpath)
        self.field_send_keys(self.level_xpath, Keys.CONTROL + "a")
        self.field_send_keys(self.level_xpath, Keys.DELETE)
        self.field_send_keys(self.youtubeField_xpath, youtube_field)
    def click_removeLinkToYoutube_button(self):
        self.wait_for_element_to_be_clickable(self.removeLinkToYoutube_xpath)
        self.click_on_the_element(self.removeLinkToYoutube_xpath)
    # TODO district

    def click_on_main_page_button(self):
        self.wait_for_element_to_be_clickable(self.main_page_xpath)
        self.click_on_the_element(self.main_page_xpath)

    def click_players_button(self):
        self.wait_for_element_to_be_clickable(self.players_xpath)
        self.click_on_the_element(self.players_xpath)

    def click_matches_button(self):
        self.wait_for_element_to_be_clickable(self.matches_xpath)
        self.click_on_the_element(self.matches_xpath)
    def click_clear_button(self):
        self.wait_for_element_to_be_clickable(self.clear_xpath)
        self.click_on_the_element(self.clear_xpath)
    def click_submit_button(self):
        self.wait_for_element_to_be_clickable(self.submit_xpath)
        self.click_on_the_element(self.submit_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.redirect_to_edit_page)
        assert self.driver.title.__contains__(self.expected_title)
        # expected title which contains only the same words
        print(self.expected_title, self.driver.title)
        time.sleep(4)
        # my current player edit page title

    # def title_of_page2(self):
    #     self.wait_for_element_to_be_clickable(self.my_current_player_button_xpath)
    #     assert self.driver.title.__contains__(self.expected_title)
    #     print(self.expected_title, self.driver.title)
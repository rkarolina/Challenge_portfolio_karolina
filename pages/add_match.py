from pages.base_page import BasePage


class AddMatch(BasePage):
    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    date_field_xpath = "// input[@type= 'date']"
    radio_match_at_home_xpath = "//input[@name='matchAtHome']"
    radio_match_out_home_xpath = "input[value='false']"
    tshirt_color_field_xpath = "input[name='tshirt']"
    league_field_xpath = "//input[@name='league']"
    time_played_field_xpath = "//input[@name='timePlayed']"
    number_field_xpath = "//input[@name='number']"
    web_match_field_xpath = "//input[@name='webMatch']"
    general_field_xpath = "//input[@name='general']"
    rating_field_xpath = "//input[@name='rating']"
    submit_button_xpath= "//*[contains(@class, 'containedPrimary')]"
    clear_button_xpath = "//*[contains(@class, 'containedSecondary')]"

    def type_in_myteam(self,myteam):
        self.wait_for_element_to_be_clickable(self.my_team_field_xpath)
        self.field_send_keys(self.my_team_field_xpath, myteam)
    def type_in_enemyteam(self,enemyteam):
        self.wait_for_element_to_be_clickable(self.enemy_team_field_xpath)
        self.field_send_keys(self.enemy_team_field_xpath, enemyteam)
    def type_in_my_team_score(self,my_team_score):
        self.wait_for_element_to_be_clickable(self.my_team_score_field_xpath)
        self.field_send_keys(self.my_team_score_field_xpath, my_team_score)
    def type_in_enemy_team_score(self,enemy_team_score):
        self.wait_for_element_to_be_clickable(self.enemy_team_score_field_xpath)
        self.field_send_keys(self.enemy_team_score_field_xpath, enemy_team_score)

    # TODO 1. Match at home/Match out home
    def type_in_match_date(self, match_date):
        self.wait_for_element_to_be_clickable(self.date_field_xpath)
        self.field_send_keys(self.date_field_xpath, match_date)
    def type_in_tshirt(self,tshirt):
        self.wait_for_element_to_be_clickable(self.tshirt_color_field_xpath)
        self.field_send_keys(self.tshirt_color_field_xpath, tshirt)
    def type_in_league(self,league):
        self.wait_for_element_to_be_clickable(self.league_field_xpath)
        self.field_send_keys(self.league_field_xpath, league)
    def type_in_timeplayed(self,timeplayed):
        self.wait_for_element_to_be_clickable(self.time_played_field_xpath)
        self.field_send_keys(self.time_played_field_xpath, timeplayed)

    def type_in_number(self, number):
        self.wait_for_element_to_be_clickable(self.number_field_xpath)
        self.field_send_keys(self.number_field_xpath, number)

    def type_in_web_match(self, web_match):
        self.wait_for_element_to_be_clickable(self.web_match_field_xpath)
        self.field_send_keys(self.web_match_field_xpath, web_match)

    def type_in_web_general(self, general):
        self.wait_for_element_to_be_clickable(self.general_field_xpath)
        self.field_send_keys(self.general_field_xpath, general)

    def type_in_rating(self, rating):
        self.wait_for_element_to_be_clickable(self.rating_field_xpath)
        self.field_send_keys(self.rating_field_xpath, rating)

    def type_in_submit(self, submit):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)
        self.field_send_keys(self.submit_button_xpath, submit)

    def type_in_clear(self, clear):
        self.wait_for_element_to_be_clickable(self.clear_button_xpath)
        self.field_send_keys(self.clear_button_xpath, clear)
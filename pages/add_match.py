from pages.base_page import BasePage


class Dashboard(BasePage):
    my_team_field_xpatch = "//input[@name='myTeam']"
    enemy_team_field_xpatch = "//input[@name='enemyTeam']"
    my_team_score_field_xpatch = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpatch = "//input[@name='enemyTeamScore']"
    date_field_xpatch = "// input[@type= 'date']"
    radio_match_at_home_xpatch = "//input[@name='matchAtHome']"
    radio_match_out_home_xpatch = "input[value='false']"
    tshirt_color_field_xpatch = "input[name='tshirt']"
    league_field_xpatch = "//input[@name='league']"
    time_played_field_xpatch = "//input[@name='timePlayed']"
    number_field_xpatch = "//input[@name='number']"
    web_match_field_xpatch = "//input[@name='webMatch']"
    general_field_xpatch = "//input[@name='general']"
    rating_field_xpatch = "//input[@name='rating']"
    submit_button_xpatch= "//*[contains(@class, 'containedPrimary')]"
    clear_button_xpatch = "//*[contains(@class, 'containedSecondary')]"
pass
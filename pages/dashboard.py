from pages.base_page import BasePage


class Dashboard(BasePage):
    MainPage_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    polski_button_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    add_player_button_xpath = "//a[contains(@href, '/en/players/add')]"
    dev_team_contact_button_xpatch = "//a[contains(@href, '://')]"
    last_created_player_text_xpatch = "//*[text()='Last created player']"
    last_created_player_button_xpatch = "//div[3]/div/div/a[1]/button/span[2]"
    last_updated_player_name_xpatch = "//*[text()='Last updated player']"
    last_updated_player_button_xpatch = "//div/div/a[2]/button/span[1]"
    last_created_match_name_xpatch = "//*[text()='Last created match']"
    last_created_match_button_xpatch = "//a[3]/button/span[1]"
    last_updated_match_name_xpatch = "//*[text()='Last updated match']"
    last_updated_match_button_xpatch = "//a[4]/button/span[1]"
    last_updated_report_name_xpatch = "//*[text()='Last updated report']"
    last_updated_report_button_xpatch = "//div/div/a[5]/button/span[1] "
    pass
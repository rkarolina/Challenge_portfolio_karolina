from pages.base_page import BasePage


class Dashboard(BasePage):
    MainPage_button_xpath = "//*[@class='MuiTypography-root MuiListItemText-primary MuiTypography-body1 MuiTypography-displayBlock']"
    players_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    polski_button_xpath = "//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = " //*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    dev_team_contact_button_xpatch = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
    tester_automated_button_xpatch = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[2]"
    last_updated_player_button_xpatch = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    last_created_match_button_xpatch = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    last_updated_match_button_xpatch = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[4]/button/span[1] "
    last_updated_report_button_xpatch = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[5]/button/span[1] "
    pass
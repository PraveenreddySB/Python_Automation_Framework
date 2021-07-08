from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By


class LoginPage:
    CCPA_Link_xpath = "//*[@id='aspnetForm']/div[4]/div[2]/div[2]/button/strong"
    NonFAI_User_xpath = "//a[@href='IDaaSLogin.aspx?t=EID']"
    UserName_textbox_xpath = "//*[@id='logonIdentifier']"
    Password_textbox_xpath = "//*[@id='password']"
    Login_button_xpath = "//*[@id='next']"
    Logout_button_ID = "ctl00_HozMenu1_ucLogout_cmdLogout"

    def __init__(self, driver):
        self.driver = driver

    def ccpalink(self):
        self.driver.find_element_by_xpath(self.CCPA_Link_xpath).click()

    def nonFAIUserLink(self):
        self.driver.find_element_by_xpath(self.NonFAI_User_xpath).click()

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.UserName_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.UserName_textbox_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.Password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.Password_textbox_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.Login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.Logout_button_ID).click()

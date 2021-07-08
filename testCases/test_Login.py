import time

import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    Logger = LogGen.loggen()

    def test_homepagetitle(self, setup):

        self.Logger.info("******************Verify HOME Page Tile******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        act_title = self.driver.title

        if act_title == "Sign In":
            assert True
            self.Logger.info("******************HOME Page PASSED******************")
            self.driver.close()
        else:
            self.Logger.error("******************HOME Page FAILED******************")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(50)

        self.loginpageObj = LoginPage(self.driver)

        self.loginpageObj.ccpalink()
        self.loginpageObj.nonFAIUserLink()
        time.sleep(10)
        self.loginpageObj.setUserName(self.username)
        self.loginpageObj.setPassword(self.password)
        self.loginpageObj.clickLogin()
        time.sleep(10)

        act_title = self.driver.title
        print(act_title)
        if act_title.replace(" ", "") == "First American Navigator".replace(" ", ""):
            self.loginpageObj.clickLogout()
            self.driver.close()
            self.Logger.info("*****PASSED******")
        else:
            self.loginpageObj.clickLogout()
            self.driver.close()
            self.Logger.error("*****FAILED******")

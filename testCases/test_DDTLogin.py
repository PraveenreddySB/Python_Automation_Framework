import time
import pytest
from selenium import webdriver
from pageObject.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from selenium.webdriver.common.by import By


class Test_DDT_Login:
    baseurl = ReadConfig.getApplicationURL()
    path = ".//TestData/TestData.xlsx"
    Logger = LogGen.loggen()

    def test_DDTlogin(self, setup):

        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.implicitly_wait(100)
        self.driver.maximize_window()

        self.loginpageObj = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "Login")
        print("Rows:", self.rows)
        lst_status = []

        for r in range(2, self.rows + 1):

            self.username = XLUtils.readData(self.path, "Login", r, 1)
            self.password = XLUtils.readData(self.path, "Login", r, 2)
            self.expected = XLUtils.readData(self.path, "Login", r, 3)

            # self.loginpageObj.ccpalink()
            self.loginpageObj.nonFAIUserLink()
            time.sleep(5)

            self.loginpageObj.setUserName(self.username)
            self.loginpageObj.setPassword(self.password)
            self.loginpageObj.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            print(act_title)
            if act_title.replace(" ", "") == "First American Navigator".replace(" ", ""):
                if self.expected == "PASS":
                    self.Logger.info("*****PASSED******")
                    self.loginpageObj.clickLogout()
                    lst_status.append("PASS")
                elif self.expected == "FAIL":
                    self.Logger.info("****FAILD****")
                    self.loginpageObj.clickLogout()
                    lst_status.append("FAIL")
            elif act_title != "First American Navigator".replace(" ", ""):
                if self.expected == "PASS":
                    self.Logger.info("***FAIL***")
                    lst_status.append("FAIL")
                elif self.expected == "FAIL":
                    self.Logger.info("*****PASSED******")
                    lst_status.append("PASS")
                print(lst_status)

        if "FAIL" not in lst_status:
            self.Logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.Logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.Logger.info("******* End of Login DDT Test **********")
        self.Logger.info("**************** Completed  TC_LoginDDT_002 ************* ");

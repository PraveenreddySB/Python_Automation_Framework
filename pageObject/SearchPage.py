from selenium import webdriver


class SearchPage:
    REO_solution_xpath = "//*[@id='ctl00_ContentPlaceHolder1_ctl03_bl-image']//*[text()='Services >']"
    REO_solution_confirm_xpath = "//*[@id='ctl00_lblSolutionName']"
    ModuleSearch_xpath = "//*[@id='liSideMenuSearch']//*[text()='Search']"

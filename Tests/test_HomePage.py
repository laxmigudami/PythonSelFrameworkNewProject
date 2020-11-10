import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info(getData)
        log.info("entering details into all the fields")
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["Email"])
        homepage.getPassword().send_keys(getData["password"])
        homepage.getCheckbox().click()
        element = homepage.getGender()
        self.selectOptionByText(element, getData["gender"])

        homepage.getRadioButton().click()
        homepage.getSuccessButton().click()
        alertText = homepage.getSuccessMsg().text
        log.info(alertText)
        assert "Success" in alertText
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param

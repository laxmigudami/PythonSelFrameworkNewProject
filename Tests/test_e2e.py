from selenium import webdriver
import pytest
import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass
from Tests.conftest import *


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkOutPage = homepage.shopItems()
        log.info("getting all the card titles")
        cards = checkOutPage.getCardTitles()
        i = -1

        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)

            if cardText == "Blackberry":
                log.info("adding item to the cart")
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.checkOutItems().click()
        confirmpage = checkOutPage.getCheckOutButton()
        log.info("entering country name as ind")

        self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresence("India")

        confirmpage.getCountryName().click()
        confirmpage.getCheckbox().click()
        confirmpage.getPurchaseButton().click()
        successMsg = confirmpage.getSuccessMsg().text
        log.info(successMsg)
        assert "Success! ghgg Thank you!" in successMsg
        self.driver.save_screenshot("test.png")


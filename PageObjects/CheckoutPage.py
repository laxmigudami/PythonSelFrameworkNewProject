from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    cardtitle = (By.CSS_SELECTOR, '.card-title a')
    cardfooter = (By.XPATH, '//button[@class="btn btn-info"]')
    checkout = (By.XPATH, '//a[@class="nav-link btn btn-primary"]')
    checkoutbutton = (By.XPATH, '//button[@class="btn btn-success"]')

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardtitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardfooter)

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def getCheckOutButton(self):
        self.driver.find_element(*CheckoutPage.checkoutbutton).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

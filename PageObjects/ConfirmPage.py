from selenium.webdriver.common.by import By


class ConfirmPage:
    countryNameInitial = (By.CSS_SELECTOR, '#country')
    countryName = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, '//div[@class="checkbox checkbox-primary"]')
    purchaseButton = (By.CSS_SELECTOR, 'input[value="Purchase"]')
    successMsg = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')

    def __init__(self, driver):
        self.driver = driver

    # def getCountryInitial(self):
    #     return self.driver.find_element(*ConfirmPage.countryNameInitial)

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.successMsg)
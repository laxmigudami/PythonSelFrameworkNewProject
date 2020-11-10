from selenium.webdriver.common.by import By

from PageObjects.CheckoutPage import CheckoutPage


class HomePage:
    shop = (By.XPATH, '//a[text()="Shop"]')
    name = (By.CSS_SELECTOR, '[name="name"]')
    email = (By.XPATH, '//input[@name="email"]')
    password = (By.XPATH, '//input[@placeholder="Password"]')
    checkbox = (By.CSS_SELECTOR, '#exampleCheck1')
    gender = (By.CSS_SELECTOR, '#exampleFormControlSelect1')
    radiobutton = (By.CSS_SELECTOR, '#inlineRadio1')
    successbutton = (By.XPATH, '//input[@class="btn btn-success"]')
    successmessage = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()  # *to deserialize the tuple shop
        checkOutPage = CheckoutPage(self.driver)
        return checkOutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getRadioButton(self):
        return self.driver.find_element(*HomePage.radiobutton)

    def getSuccessButton(self):
        return self.driver.find_element(*HomePage.successbutton)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successmessage)

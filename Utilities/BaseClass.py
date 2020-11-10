import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setUp")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, element, text):    
        sel = Select(element)
        sel.select_by_visible_text(text)

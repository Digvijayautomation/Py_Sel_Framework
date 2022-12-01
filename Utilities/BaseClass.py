import inspect
import logging

import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")  # This will trigger setup method from conftest
class BaseClass:


    # Method for Explicit wait for checking presence of element
    def presense_of_element(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, element)))

    # Method for Explicit wait for checking element is clickable
    # We can call this method directly in our test case as  self.element_is_clickable("element")
    def element_is_clickable(self, element):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, element)))

    def get_logger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger





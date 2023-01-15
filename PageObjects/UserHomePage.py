from selenium.webdriver.common.by import By

from PageObjects.Add_Employee import Add_Employee


class UserHomePage:

    def __init__(self, driver):  # Constructor with driver parameter so that we can use same driver from test class
        self.driver = driver

    # Locators
    PIM_Link = (By.XPATH, "//span[text()= 'PIM']")
    Add_Employee_Button = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

    # Methods
    def pim_link_text(self):
        return self.driver.find_element(*UserHomePage.PIM_Link).text

    def pim_link(self):
        return self.driver.find_element(*UserHomePage.PIM_Link)

    def add_employee_button(self):
        self.driver.find_element(*UserHomePage.Add_Employee_Button).click()
        AE = Add_Employee(self.driver)
        return AE  # returning this because after clicking add it will redirect to employee add page

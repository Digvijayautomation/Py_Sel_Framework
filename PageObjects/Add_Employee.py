from selenium.webdriver.common.by import By

from PageObjects.Logout import Logout


class Add_Employee:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    Employee_Fname = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-firstname']")
    Employee_Mname = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-middlename']")
    Employee_Lname = (By.XPATH, "//input[@class='oxd-input oxd-input--active orangehrm-lastname']")
    Submit = (By.XPATH, "//button[@type='submit']")

    def enter_name(self):
        return self.driver.find_element(*Add_Employee.Employee_Fname)

    def enter_mname(self):
        return self.driver.find_element(*Add_Employee.Employee_Mname)

    def enter_lname(self):
        return self.driver.find_element(*Add_Employee.Employee_Lname)

    def submit(self):
        self.driver.find_element(*Add_Employee.Submit).click()
        logout = Logout(self.driver)
        return logout  # returning this because after clicking add it will redirect to employee add page



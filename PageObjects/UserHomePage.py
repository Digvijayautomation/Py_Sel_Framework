from selenium.webdriver.common.by import By


class UserHomePage:

    def __init__(self, driver):  # Constructor with driver parameter so that we can use same driver from test class
        self.driver = driver

    # Locators
    Admin_Link = (By.XPATH, "//span[text()= 'Admin']")
    Add_Employee_Button = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")

    # Methods
    def admin_link(self):
        return self.driver.find_element(*UserHomePage.Admin_Link)

    def add_employee_button(self):
        return self.driver.find_element(*UserHomePage.Add_Employee_Button)

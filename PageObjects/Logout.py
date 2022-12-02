from selenium.webdriver.common.by import By


class Logout:

    def __init__(self, driver):  # Constructor with driver parameter so that we can use same driver from test class
        self.driver = driver

    # Locators

    Account_Tab=(By.XPATH,"//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']")
    Logout=(By.XPATH,"//a[@href='/web/index.php/auth/logout']")



    def click_account_tab(self):
        return self.driver.find_element(*Logout.Account_Tab)

    def click_logout(self):
        return self.driver.find_element(*Logout.Logout)
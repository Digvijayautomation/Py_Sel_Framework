from selenium.webdriver.common.by import By

from PageObjects.UserHomePage import UserHomePage


class HomePage:

    def __init__(self, driver):  # Constructor with driver parameter so that we can use same driver from test class
        self.driver = driver

    # Locators

    Username = (By.XPATH, "//input[@name='username']")
    Password = (By.XPATH, "//input[@name='password']")
    Login_Button = (By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")

    # Used * so that it will deserialize it and consider it as tuple like (By.XPATH, "//span[text()='Sign In']")
    # Methods

    def send_username(self):
        return self.driver.find_element(*HomePage.Username)

    def send_password(self):
        return self.driver.find_element(*HomePage.Password)

    # After this method we are going to UserHomePage, so we are returning that page here
    # by doing click action here only and creating object of UserHomePage here
    def click_login(self):
        self.driver.find_element(*HomePage.Login_Button).click()
        UHP = UserHomePage(self.driver)
        return UHP

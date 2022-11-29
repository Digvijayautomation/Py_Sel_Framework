
from PageObjects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestMain(BaseClass):

    def test_login(self):
        # Object Of HomePage Class
        HP = HomePage(self.driver)

        # Object of HomePage Only created, object for HomePage is created in HomePage's so that i will return UserHomePage,
        # we are chaining pages functionality wise

        # Passing Methods From HomePage, And Doing Actions On Them As Per The Need
        HP.send_username().send_keys("Admin")
        HP.send_password().send_keys("admin123")

        UHP = HP.click_login()  # Click in done in page object, and returned object of UserHomePage

        UHP.admin_link().click()
        UHP.add_employee_button().click()

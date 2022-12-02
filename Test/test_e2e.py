import pytest

from PageObjects.HomePage import HomePage
from TestData import test_dataexcel
from TestData.test_data import test_data
from TestData.test_dataexcel import testdataexcel
from Utilities.BaseClass import BaseClass


class TestMain(BaseClass):

    def test_login(self, getdata):  # getdata for passing data from fixture data provider

        log = self.get_logger()  # Object of logger class

        # Object Of HomePage Class
        HP = HomePage(self.driver)

        # Object of HomePage Only created, object for HomePage is created in HomePage's so that i will return UserHomePage,
        # we are chaining pages functionality wise

        # Passing Methods From HomePage, And Doing Actions On Them As Per The Need
        HP.send_username().send_keys(getdata["username"])
        log.info("Username Send")

        HP.send_password().send_keys(getdata["password"])
        log.info("Password Send")

        UHP = HP.click_login()  # Click in done in page object, and returned object of UserHomePage
        log.info("Login Button Clicked")

        UHP.pim_link().click()
        log.info("PIM Link Clicked")

        AE = UHP.add_employee_button()  # Click in done in page object, and returned object of Add Employee
        AE.enter_name().send_keys(getdata["fname"])
        AE.enter_mname().send_keys(getdata["mname"])
        AE.enter_lname().send_keys(getdata["lname"])

        logout = AE.submit()  # Click in done in page object, and returned logout page
        logout.click_account_tab().click()
        logout.click_logout().click()

    # We can also use fixture as data provider using python dictionary
    # We can store that data into separate file and access that file (like dict, excel)
    # We can pass multiple sets of data also (valid and invalid)

    # Data from Dict(test_data)
    @pytest.fixture(params=test_data.testdata)  # we can import that class
    def getdata(self, request):
        return request.param

# Data from Dict(test_data_using_excel)
#     @pytest.fixture(params=testdataexcel.data_excel("T1"))  # we can import that class And the name of test case which we want to run
#     def getdata(self, request):
#      return request.param

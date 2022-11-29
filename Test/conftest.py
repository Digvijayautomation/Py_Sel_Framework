import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# For passing browser as command line arugment

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# Fixture
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_Object = Service("C://Users//digvijayt//Documents//chromedriver_win32//chromedriver.exe")
        driver = webdriver.Chrome(service=service_Object)
        driver.implicitly_wait(10)
    elif browser_name == "edge":
        service_Object = Service("C://Users//digvijayt//Documents//edgedriver_win32//msedgedriver.exe")
        driver = webdriver.Edge(service=service_Object)
        driver.implicitly_wait(10)

   #Afrer Choosing The Browser Hit URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()

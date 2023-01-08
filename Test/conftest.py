import pytest
from selenium import webdriver

driver = None


# For passing browser as command line argument

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# Fixture
@pytest.fixture(scope="class")
def setup(request):
    global driver

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()  # From selenium version 4 we can use it directly
        driver.implicitly_wait(10)

    elif browser_name == "edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(10)

    # After Choosing The Browser Hit URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()

    # Code for attaching screenshot of failed test cases to html report

    @pytest.mark.hookwrapper
    def pytest_runtest_makereport(item):
        """
            Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
            :param item:
            """
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, 'extra', [])

        if report.when == 'call' or report.when == "setup":
            xfail = hasattr(report, 'wasxfail')
            if (report.skipped and xfail) or (report.failed and not xfail):
                file_name = report.nodeid.replace("::", "_") + ".png"
                capture_screenshot(file_name)
                if file_name:
                    html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                           'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def capture_screenshot(name):
        driver.get_screenshot_as_file(name)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
import pytest
from utils import utils as UT


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser")


@pytest.fixture(scope="class")
def test_setup(request):
    browser = request.config.getoption("--browser")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

        # driver = webdriver.Chrome(
        #     executable_path="C:\\Users\\ansarar\\SeleniumProjects\\AutomationFrameworkPractice\\drivers\\chromedriver.exe")
    elif browser == "ie":
        driver = webdriver.Ie(IEDriverManager().install())
        # driver = webdriver.Chrome(
        #     executable_path="C:\\Users\\ansarar\\SeleniumProjects\\AutomationFrameworkPractice\\drivers\\geckodriver.exe")
    else:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    driver.implicitly_wait(20)
    driver.maximize_window()
    driver.get(UT.URL)
    request.cls.driver = driver
    yield
    driver.quit()
    print("test completed")
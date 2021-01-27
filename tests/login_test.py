import moment
from selenium.common import exceptions as ex
import allure
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as ut


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(ut.USERNAME)
        login.enter_password(ut.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            home = HomePage(driver)
            home.click_welcome()
            home.click_logout()
            page_tittle = driver.title
            assert page_tittle == "OrangeHR"

        except ex.ElementNotVisibleException:
            currenttime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testname = ut.whoami()
            screenshotname = testname + "_" + currenttime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotname,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:\\Users\\ansarar\\SeleniumProjects\\AutomationFrameworkPractice\\screenshots\\" +
                                          screenshotname + ".png")
            raise

        except AssertionError as error :
            print("assertion error")
            print(error)
            currenttime = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            testname = ut.whoami()
            screenshotname = testname + "_" + currenttime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotname,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:\\Users\\ansarar\\SeleniumProjects\\AutomationFrameworkPractice\\screenshots\\" +
                screenshotname + ".png")
            raise
        except:
            print("in exceopt")
            raise
        else:
            print("")

        finally:
            print("in finally")

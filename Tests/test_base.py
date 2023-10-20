import pytest

from Config.config import TestData
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    def login(self, page_name, value):
        self.loginPage = LoginPage(self.driver)
        # if self.loginPage.access_localstorage() == 1:
        if value == 1:
            test_page = self.loginPage.login_return_to_test_page(page_name)
        else:
            test_page = self.loginPage.login_return_to_test_page(page_name,
                                                            TestData.ADMIN_EMAIL,
                                                            TestData.ADMIN_PASSWORD)
        return test_page

    def login1(self, page_name):
        self.loginPage = LoginPage(self.driver)
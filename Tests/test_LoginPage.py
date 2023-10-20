from Config.config import TestData
from Tests.test_base import BaseTest
from pages.LoginPage import LoginPage
import gc


class TestLogin(BaseTest):

    def test_check_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.check_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE

    def test_check_require_msg(self):
        self.loginPage = LoginPage(self.driver)
        error_msg = self.loginPage.check_require_msg("", "")
        assert error_msg == TestData.ERROR_MSG

    def test_check_invalid_msg(self):
        self.loginPage = LoginPage(self.driver)
        invalid_msg = self.loginPage.check_require_msg("abd")
        assert invalid_msg[0] == TestData.EMAIL_FAIL_MSG

    def test_check_placeholder_msg(self):
        self.loginPage = LoginPage(self.driver)
        placeholder = self.loginPage.check_placeholder()
        assert placeholder == TestData.PLACEHOLDER

    def test_login_attempt_1(self):
        self.loginPage = LoginPage(self.driver)
        msg = self.loginPage.fail_login("test@gmail.com", "test@123")
        assert msg == TestData.EMAIL_FAIL_MSG

    def test_login_attempt_2(self):
        self.loginPage = LoginPage(self.driver)
        self.driver.refresh()
        msg = self.loginPage.fail_login("yogesh@scrapyard.com", "test@123")
        assert msg == TestData.PASSWORD_FAIL_MSG

    def test_login_attempt_3(self):
        self.loginPage = LoginPage(self.driver)
        self.driver.refresh()
        msg = self.loginPage.do_login(TestData.ADMIN_EMAIL, TestData.ADMIN_PASSWORD)
        assert msg == TestData.SUCCESS_LOGIN


gc.collect()


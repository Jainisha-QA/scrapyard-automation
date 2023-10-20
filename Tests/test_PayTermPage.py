import gc

from Config.config import TestData
from Tests.test_base import BaseTest


class TestContainerPage(BaseTest):

    def test_load_url(self):
        pay_term_page = self.login("PayTermPage", 0)
        assert pay_term_page.check_url(TestData.PAYTERMS_URL)

    def test_check_require_msg_and_placeholder(self):
        pay_term_page = self.login("PayTermPage", 1)
        msg = pay_term_page.check_require_msg()
        assert msg == TestData.PAY_TERM_REQUIRE
        msg = pay_term_page.check_placeholder()
        assert msg == TestData.PAYTERMS_PLACEHOLDER

    def test_add_payterm(self):
        pay_term_page = self.login("PayTermPage", 1)
        msg = pay_term_page.add_fun("az")
        assert msg == TestData.DATA_ADD_MSG

    def test_update_payterm(self):
        pay_term_page = self.login("PayTermPage", 1)
        pay_term_page.search_fun("az")
        msg = pay_term_page.update_fun("az", "axyz")
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_payterm(self):
        pay_term_page = self.login("PayTermPage", 1)
        pay_term_page.search_fun("axyz")
        msg = pay_term_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

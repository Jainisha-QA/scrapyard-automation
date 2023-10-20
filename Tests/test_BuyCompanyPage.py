import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestBuyCompanyPage(BaseTest):

    def test_load_url(self):
        mat_page = self.login("BuyCompanyPage", 0)
        assert mat_page.check_url(TestData.BUYCOMPANY_URL)

    def test_check_require_msg_and_placeholder(self):
        mat_page = self.login("BuyCompanyPage", 1)
        msg0, msg1, msg2 = mat_page.check_require_msg()
        assert msg0 == TestData.BUYGUP1_REQUIRE
        assert msg1 == TestData.BUYCOMNAME_REQUIRE
        assert msg2 == TestData.ADDRESS_REQUIRE
        msg1, msg2 = mat_page.check_placeholder()
        assert msg1 == TestData.BUYCOM_PLACEHOLDER
        assert msg2 == TestData.ADDRESS_PLACEHOLDER

    def test_add_buycompany(self):
        mat_page = self.login("BuyCompanyPage", 1)
        msg = mat_page.add_fun(["az", "1aa1"])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_buycompany(self):
        mat_page = self.login("BuyCompanyPage", 1)
        time.sleep(5)
        mat_page.search_fun("az")
        msg = mat_page.update_fun("az", ["axyz","1bb1"])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_buycompany(self):
        mat_page = self.login("BuyCompanyPage", 1)
        time.sleep(3)
        mat_page.search_fun("axyz")
        msg = mat_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()


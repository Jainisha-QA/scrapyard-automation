import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestBuyGupPage(BaseTest):

    def test_load_url(self):
        buy_gup_page = self.login("BuyGupPage", 0)
        assert buy_gup_page.check_url(TestData.BUYGROUP_URL)

    def test_check_require_msg_and_placeholder(self):
        buy_gup_page = self.login("BuyGupPage", 1)
        msg0, msg1 = buy_gup_page.check_require_msg()
        assert msg0 == TestData.BUYGUP_NAME_REQUIRE
        assert msg1 == TestData.ADDRESS_REQUIRE
        msg0, msg1 = buy_gup_page.check_placeholder()
        assert msg0 == TestData.BUYGUP_PLACEHOLDER
        assert msg1 == TestData.ADDRESS_PLACEHOLDER

    def test_add_buygup(self):
        buy_gup_page = self.login("BuyGupPage", 1)
        msg = buy_gup_page.add_fun(["az", "sjhdkjs#$#"])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_buygup(self):
        buy_gup_page = self.login("BuyGupPage", 1)
        buy_gup_page.search_fun("az")
        msg = buy_gup_page.update_fun("az", ["axyz", "kmdsfks#$"])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_buygup(self):
        buy_gup_page = self.login("BuyGupPage", 1)
        time.sleep(3)
        buy_gup_page.search_fun("axyz")
        msg = buy_gup_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()


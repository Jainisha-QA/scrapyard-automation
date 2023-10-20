import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestBuyCompanyPage(BaseTest):

    def test_load_url(self):
        buy_com_page = self.login("BuyEmpPage", 0)
        assert buy_com_page.check_url(TestData.BUYEMP_URL)

    def test_check_require_msg_and_placeholder(self):
        buy_com_page = self.login("BuyEmpPage", 1)
        buy_com_page.check_require_msg()
        msg0, msg1, msg2, msg3, msg4, msg5 = buy_com_page.check_require_msg()
        assert msg0 == TestData.BUYGUP1_REQUIRE
        assert msg1 == TestData.BUYCOM_REQUIRE
        assert msg2 == TestData.FNAME_REQUIRE
        assert msg3 == TestData.LNAME_REQUIRE
        assert msg4 == TestData.EMAIL_REQUIRE
        assert msg5 == TestData.PASSWORD_REQUIRE
        msg1, msg2, msg3, msg4= buy_com_page.check_placeholder()
        assert msg1 == TestData.FNAME_PLACEHOLDER
        assert msg2 == TestData.LNAME_PLACEHOLDER
        assert msg3 == TestData.EMAIL_PLACEHOLDER
        assert msg4 == TestData.PASSWORD_PLACEHOLDER

    def test_add_buyemp(self):
        buy_com_page = self.login("BuyEmpPage", 1)
        msg = buy_com_page.add_fun(["az", "1aa1", '1', '2'])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_buyemp(self):
        buy_com_page = self.login("BuyEmpPage", 1)
        time.sleep(5)
        buy_com_page.search_fun("az")
        msg = buy_com_page.update_fun("az", ["axyz","1bb1", '0', '1'])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_buyemp(self):
        buy_com_page = self.login("BuyEmpPage", 1)
        time.sleep(3)
        buy_com_page.search_fun("axyz")
        msg = buy_com_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

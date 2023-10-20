import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestSupCompanyPage(BaseTest):

    def test_load_url(self):
        sup_com_page = self.login("SupCompanyPage", 0)
        assert sup_com_page.check_url(TestData.SUPCOMPANY_URL)

    def test_check_require_msg_and_placeholder(self):
        sup_com_page = self.login("SupCompanyPage", 1)
        msg0, msg1, msg2, msg3, msg4, msg5 = sup_com_page.check_require_msg()
        assert msg0 == TestData.SUPGUP_REQUIRE
        assert msg1 == TestData.NAME_REQUIRE
        assert msg2 == TestData.ADDRESS_REQUIRE
        assert msg3 == TestData.TAX_REQUIRE
        assert msg4 == TestData.EXPORTER_REQUIRE
        assert msg5 == TestData.GST_REQUIRE
        msg1, msg2, msg3, msg4, msg5 = sup_com_page.check_placeholder()
        assert msg1 == TestData.NAME_PLACEHOLDER
        assert msg2 == TestData.ADDRESS_PLACEHOLDER
        assert msg3 == TestData.TAX_PLACEHOLDER
        assert msg4 == TestData.EXPORTER_PLACEHOLDER
        assert msg5 == TestData.GST_PLACEHOLDER

    def test_add_supcompany(self):
        sup_com_page = self.login("SupCompanyPage", 1)
        msg = sup_com_page.add_fun(["az", "1aa1", '1', '2', '3'])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_supcompany(self):
        sup_com_page = self.login("SupCompanyPage", 1)
        time.sleep(5)
        sup_com_page.search_fun("az")
        msg = sup_com_page.update_fun("az", ["axyz","1bb1", '0', '1', '2'])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_supcompany(self):
        sup_com_page = self.login("SupCompanyPage", 1)
        time.sleep(3)
        sup_com_page.search_fun("axyz")
        msg = sup_com_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

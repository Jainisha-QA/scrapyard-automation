import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestSupGupPage(BaseTest):

    def test_load_url(self):
        sup_gup_page = self.login("SupGupPage", 0)
        assert sup_gup_page.check_url(TestData.SUPGROUP_URL)

    def test_check_require_msg_and_placeholder(self):
        sup_gup_page = self.login("SupGupPage", 1)
        msg0, msg1 = sup_gup_page.check_require_msg()
        assert msg0 == TestData.SUPGUP_REQUIRE
        assert msg1 == TestData.COUNTRY_REQUIRE
        msg = sup_gup_page.check_placeholder()
        assert msg == TestData.SUPGUP_PLACEHOLDER

    def test_add_supgup(self):
        sup_gup_page = self.login("SupGupPage", 1)
        msg = sup_gup_page.add_fun("az")
        assert msg == TestData.DATA_ADD_MSG

    def test_update_supgup(self):
        sup_gup_page = self.login("SupGupPage", 1)
        time.sleep(3)
        sup_gup_page.search_fun("az")
        msg = sup_gup_page.update_fun("az", "axyz")
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_supgup(self):
        sup_gup_page = self.login("SupGupPage", 1)
        time.sleep(3)
        sup_gup_page.search_fun("axyz")
        msg = sup_gup_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

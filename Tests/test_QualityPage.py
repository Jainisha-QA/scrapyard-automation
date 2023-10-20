import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestQualityPage(BaseTest):

    def test_load_url(self):
        quality_page = self.login("QualityPage", 0)
        assert quality_page.check_url(TestData.QUALITY_URL)

    def test_check_require_msg_and_placeholder(self):
        quality_page = self.login("QualityPage", 1)
        msg = quality_page.check_require_msg()
        time.sleep(2)
        assert msg == TestData.NAME_REQUIRE
        msg1, msg2 = quality_page.check_placeholder()
        assert msg1 == TestData.NAME_PLACEHOLDER
        assert msg2 == TestData.DESC_PLACEHOLDER

    def test_add_quality(self):
        quality_page = self.login("QualityPage", 1)
        msg = quality_page.add_fun(["az", "Aham#$$%"])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_quality(self):
        quality_page = self.login("QualityPage", 1)
        quality_page.search_fun("az")
        msg = quality_page.update_fun("az", ["axyz", "Kem cho?"])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_quality(self):
        quality_page = self.login("QualityPage", 1)
        quality_page.search_fun("axyz")
        msg = quality_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

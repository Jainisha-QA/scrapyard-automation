import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestMatCategory(BaseTest):

    def test_load_url(self):
        mat_page = self.login("MatPage", 0)
        assert mat_page.check_url(TestData.MAT_URL)

    def test_check_require_msg_and_placeholder(self):
        mat_page = self.login("MatPage", 1)
        msg0, msg1, msg2 = mat_page.check_require_msg()
        assert msg0 == TestData.MAT_CAT_REQUIRE
        assert msg1 == TestData.NAME_REQUIRE
        assert msg2 == TestData.HS_CODE_REQUIRE
        msg0, msg1 = mat_page.check_placeholder()
        assert msg0 == TestData.MAT_NAME_PLACEHOLDER
        assert msg1 == TestData.MAT_HSCODE_PLACEHOLDER

    def test_add_mat(self):
        mat_page = self.login("MatPage", 1)
        msg = mat_page.add_fun("az", "1aa1")
        assert msg == TestData.DATA_ADD_MSG

    def test_update_mat(self):
        mat_page = self.login("MatPage", 1)
        time.sleep(5)
        mat_page.search_fun("az")
        msg = mat_page.update_fun("az", ["axyz","1bb1"])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_mat(self):
        mat_page = self.login("MatPage", 1)
        time.sleep(5)
        mat_page.search_fun("axyz")
        msg = mat_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

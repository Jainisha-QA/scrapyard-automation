import gc
import time
from Config.config import TestData
from Tests.test_base import BaseTest


class TestMatCategory(BaseTest):

    def test_load_url(self):
        matCategory_page = self.login("MatCategoryPage", 0)
        # matCategory_page.load_test_page()
        assert matCategory_page.check_url(TestData.MATCATEGORY_URL)

    def test_check_require_msg_and_placeholder(self):
        matCategory_page = self.login("MatCategoryPage", 1)
        msg = matCategory_page.check_require_msg()
        assert msg == TestData.NAME_REQUIRE
        placeholder = matCategory_page.check_placeholder()
        assert placeholder == TestData.MAT_CAT_PLACEHOLDER

    def test_add_mat_category(self):
        matCategory_page = self.login("MatCategoryPage", 1)
        msg = matCategory_page.add_fun("az")
        assert msg == TestData.DATA_ADD_MSG

    def test_update_mat_category(self):
        matCategory_page = self.login("MatCategoryPage", 1)
        matCategory_page.search_fun("az")
        msg = matCategory_page.update_fun("az", "axyz")
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_mat_category(self):
        matCategory_page = self.login("MatCategoryPage", 1)
        matCategory_page.search_fun("axyz")
        msg = matCategory_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

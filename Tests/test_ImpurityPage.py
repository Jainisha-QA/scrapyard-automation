import gc

from Config.config import TestData
from Tests.test_base import BaseTest


class TestImpurityPage(BaseTest):

    def test_load_url(self):
        impurity_page = self.login("ImpurityPage", 0)
        assert impurity_page.check_url(TestData.IMPURITY_URL)

    def test_check_require_msg_and_placeholder(self):
        impurity_page = self.login("ImpurityPage", 1)
        msg = impurity_page.check_require_msg()
        assert msg == TestData.IMPURITY_REQUIRE
        msg = impurity_page.check_placeholder()
        assert msg == TestData.IMPURITY_PLACEHOLDER

    def test_add_impurity(self):
        impurity_page = self.login("ImpurityPage", 1)
        msg = impurity_page.add_fun("az")
        assert msg == TestData.DATA_ADD_MSG

    def test_update_impurity(self):
        impurity_page = self.login("ImpurityPage", 1)
        impurity_page.search_fun("az")
        msg = impurity_page.update_fun("az", "axyz")
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_impurity(self):
        impurity_page = self.login("ImpurityPage", 1)
        impurity_page.search_fun("axyz")
        msg = impurity_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

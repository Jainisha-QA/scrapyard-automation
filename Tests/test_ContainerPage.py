import gc

from Config.config import TestData
from Tests.test_base import BaseTest


class TestContainerPage(BaseTest):

    def test_load_url(self):
        container_page = self.login("ContainerPage", 0)
        assert container_page.check_url(TestData.CONTAINERS_URL)

    def test_check_test_require_and_placeholder(self):
        container_page = self.login("ContainerPage", 1)
        msg = container_page.check_require_msg()
        assert msg == TestData.NAME_REQUIRE
        msg = container_page.check_placeholder()
        assert msg == TestData.CONTAINER_PLACEHOLDER

    def test_add_container(self):
        container_page = self.login("ContainerPage", 1)
        msg = container_page.add_fun("az")
        assert msg == TestData.DATA_ADD_MSG

    def test_update_container(self):
        container_page = self.login("ContainerPage", 1)
        container_page.search_fun("az")
        msg = container_page.update_fun("az", "axyz")
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_container(self):
        container_page = self.login("ContainerPage", 1)
        container_page.search_fun("axyz")
        msg = container_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

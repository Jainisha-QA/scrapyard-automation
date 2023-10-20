import gc

from Config.config import TestData
from Tests.test_base import BaseTest


class TestPlantPage(BaseTest):

    def test_load_url(self):
        pay_term_page = self.login("PlantPage", 0)
        assert pay_term_page.check_url(TestData.PLANT_URL)

    def test_check_require_msg_and_placeholder(self):
        pay_term_page = self.login("PlantPage", 1)
        msg0, msg1, msg2 = pay_term_page.check_require_msg()
        assert msg0 == TestData.ADDRESS_REQUIRE
        assert msg1 == TestData.OFFLOADING_REQUIRE
        assert msg2 == TestData.PRODUCTION_REQUIRE
        msg0, msg1, msg2 = pay_term_page.check_placeholder()
        assert msg0 == TestData.ADDRESS_PLACEHOLDER
        assert msg1 == TestData.OFF_CAPACITY_PLACEHOLDER
        assert msg2 == TestData.PRODUCTION_PLACEHOLDER

    def test_add_plant(self):
        pay_term_page = self.login("PlantPage", 1)
        msg = pay_term_page.add_fun(["az", "6 KG", "10 KG"])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_plant(self):
        pay_term_page = self.login("PlantPage", 1)
        pay_term_page.search_fun("az")
        msg = pay_term_page.update_fun("az", ["axyz", "7 KG", "12 KG"])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_plant(self):
        pay_term_page = self.login("PlantPage", 1)
        pay_term_page.search_fun("axyz")
        msg = pay_term_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

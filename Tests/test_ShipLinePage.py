import gc

from Config.config import TestData
from Tests.test_base import BaseTest


class TestShipLinePage(BaseTest):

    def test_load_url(self):
        ship_line_page = self.login("ShipLinePage", 0)
        assert ship_line_page.check_url(TestData.SHIPPING_LINE_URL)

    def test_check_require_msg(self):
        ship_line_page = self.login("ShipLinePage", 1)
        msg = ship_line_page.check_require_msg()
        assert msg == TestData.NAME_REQUIRE
        msg0, msg1, msg2 = ship_line_page.check_placeholder()
        assert msg0 == TestData.NAME_PLACEHOLDER
        assert msg1 == TestData.LINK_PLACEHOLDER
        assert msg2 == TestData.API_PLACEHOLDER

    def test_add_shipline(self):
        ship_line_page = self.login("ShipLinePage", 1)
        msg = ship_line_page.add_fun(["az", "", ""])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_shipline(self):
        ship_line_page = self.login("ShipLinePage", 1)
        ship_line_page.search_fun("az")
        msg = ship_line_page.update_fun("az", ["axyz", "sdkfj", "api/ui"])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_shipline(self):
        ship_line_page = self.login("ShipLinePage", 1)
        ship_line_page.search_fun("axyz")
        msg = ship_line_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

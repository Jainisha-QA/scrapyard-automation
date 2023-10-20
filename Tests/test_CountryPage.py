import gc

from Config.config import TestData
from Tests.test_base import BaseTest


class TestCountryPage(BaseTest):

    def test_load_url(self):
        country_page = self.login("CountryPage", 0)
        assert country_page.check_url(TestData.COUNTRY_URL)

    def test_check_require_msg_and_placeholder(self):
        country_page = self.login("CountryPage", 1)
        msg = country_page.check_require_msg()
        assert msg == TestData.NAME_REQUIRE
        placeholder = country_page.check_placeholder()
        assert placeholder == TestData.COUNTRY_PLACEHOLDER

    def test_add_country(self):
        country_page = self.login("CountryPage", 1)
        msg = country_page.add_fun("az")
        assert msg == TestData.DATA_ADD_MSG

    def test_update_country(self):
        country_page = self.login("CountryPage", 1)
        country_page.search_fun("az")
        msg = country_page.update_fun("az", "axyz")
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_country(self):
        country_page = self.login("CountryPage", 1)
        country_page.search_fun("axyz")
        msg = country_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

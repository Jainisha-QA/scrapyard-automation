import gc

from Config.config import TestData
from Tests.test_base import BaseTest
from pages.LoginPage import LoginPage


class TestDashboard(BaseTest):

    def test_full_screen(self):
        dashboard_page = self.login("DashBoardPage")
        assert dashboard_page.check_url(TestData.DASHBOARD_URL)
        dashboard_page.check_full_screen("\scr1.png")


gc.collect()
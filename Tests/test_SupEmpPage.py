import gc
import time

from Config.config import TestData
from Tests.test_base import BaseTest


class TestSupCompanyPage(BaseTest):

    def test_load_url(self):
        sup_emp_page = self.login("SupEmpPage", 0)
        assert sup_emp_page.check_url(TestData.SUPEMP_URL)

    def test_check_require_msg_and_placeholder(self):
        sup_emp_page = self.login("SupEmpPage", 1)
        msg0, msg1, msg2, msg3, msg4, msg5 = sup_emp_page.check_require_msg()
        assert msg0 == TestData.SUPGUP_REQUIRE
        assert msg1 == TestData.SUPCOM_REQUIRE
        assert msg2 == TestData.FNAME_REQUIRE
        assert msg3 == TestData.LNAME_REQUIRE
        assert msg4 == TestData.DESIGNATION_REQUIRE
        assert msg5 == TestData.PASSWORD_REQUIRE
        msg0, msg1, msg2, msg3 = sup_emp_page.check_placeholder()
        assert msg0 == TestData.FNAME_PLACEHOLDER
        assert msg1 == TestData.LNAME_PLACEHOLDER
        assert msg2 == TestData.DESIGNATION_PLACEHOLDER
        assert msg3 == TestData.PASSWORD_PLACEHOLDER


    def test_add_supemp(self):
        sup_emp_page = self.login("SupEmpPage", 1)
        msg = sup_emp_page.add_fun(["az", "1aa1", '1', '2', '3'])
        assert msg == TestData.DATA_ADD_MSG

    def test_update_supemp(self):
        sup_emp_page = self.login("SupEmpPage", 1)
        time.sleep(5)
        sup_emp_page.search_fun("az")
        msg = sup_emp_page.update_fun("az", ["axyz","1bb1", '0', '1', '2'])
        assert msg == TestData.DATA_UPDATE_MSG

    def test_delete_supemp(self):
        sup_emp_page = self.login("SupEmpPage", 1)
        time.sleep(3)
        sup_emp_page.search_fun("axyz")
        msg = sup_emp_page.delete_fun("axyz")
        assert msg == TestData.DATA_DELETE_MSG


gc.collect()

from selenium.webdriver.common.by import By
from Config.config import TestData
from Utils.BasePage import BasePage
from pages.BuyCompanyPage import BuyCompanyPage
from pages.BuyEmpPage import BuyEmpPage
from pages.BuyGupPage import BuyGupPage
from pages.ContainerPage import ContainerPage
from pages.CountryPage import CountryPage
from pages.DashboardPage import DashboardPage
from pages.ImpurityPage import ImpurityPage
from pages.MatCategoryPage import MatCategoryPage
from pages.MatPage import MatPage
from pages.PayTermPage import PayTermPage
from pages.PlantPage import PlantPage
from pages.PortPage import PortPage
from pages.QualityPage import QualityPage
from pages.ShipLinePage import ShipLinePage
from pages.SupCompanyPage import SupCompanyPage
from pages.SupEmpPage import SupEmpPage
from pages.SupGupPage import SupGupPage


class LoginPage(BasePage):
    EMAIL = (By.ID, "mat-input-0")
    EMAIL_ERROR = (By.ID, "mat-mdc-error-0")
    PASSWORD = (By.ID, "mat-input-1")
    PASSWORD_ERROR = (By.ID, "mat-mdc-error-1")
    SIGNIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    TOAST_MSG = (By.ID, "toast-container")
    LOADER = (By.XPATH, "//p[contains(text(),'Loading...')]")

    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url == 'data:,':
            self.driver.get(TestData.BASE_URL)
        elif self.driver.current_url == TestData.BASE_URL:
            pass
        '''else:
            user = self.access_localstorage()
            print(user)'''

    def check_title(self, title):
        return self.get_title(title)

    def check_require_msg(self, email, password=None):
        self.do_send_keys(self.EMAIL, email)
        if password is not None:
            self.do_send_keys(self.PASSWORD, password)
            error_msg = [self.get_text(self.EMAIL_ERROR), self.get_text(self.PASSWORD_ERROR)]
        else:
            error_msg = [self.get_text(self.EMAIL_ERROR)]
        # c = self.get_element_border_color(self.EMAIL)
        # c = self.get_element_border_color(self.PASSWORD)
        return error_msg

    def check_placeholder(self):
        placeholder = [self.get_attribute_element(self.EMAIL, "placeholder"),
                       self.get_attribute_element(self.PASSWORD, "placeholder")]
        return placeholder

    def enter_input(self, email, password):
        self.do_send_keys(self.EMAIL, email)
        self.do_send_keys(self.PASSWORD, password)

    def fail_login(self, email, password):
        self.enter_input(email, password)
        self.do_click(self.SIGNIN_BUTTON)
        return self.get_text(self.TOAST_MSG)

    def do_login(self, email, password):
        self.enter_input(email, password)
        self.do_click(self.SIGNIN_BUTTON)
        return self.get_text(self.TOAST_MSG)

    def login_return_to_test_page(self, test_page, email=None, password=None):
        if email is not None and password is not None:
            self.enter_input(email, password)
            self.do_click(self.SIGNIN_BUTTON)
            self.check_url(TestData.DASHBOARD_URL)

        if test_page == "DashBoardPage":  # give test page name
            return DashboardPage(self.driver)
        elif test_page == "MatCategoryPage":
            return MatCategoryPage(self.driver)
        elif test_page == "MatPage":
            return MatPage(self.driver)
        elif test_page == "CountryPage":
            return CountryPage(self.driver)
        elif test_page == "ContainerPage":
            return ContainerPage(self.driver)
        elif test_page == "PayTermPage":
            return PayTermPage(self.driver)
        elif test_page == "ImpurityPage":
            return ImpurityPage(self.driver)
        elif test_page == "QualityPage":
            return QualityPage(self.driver)
        elif test_page == "PlantPage":
            return PlantPage(self.driver)
        elif test_page == "SupGupPage":
            return SupGupPage(self.driver)
        elif test_page == "BuyGupPage":
            return BuyGupPage(self.driver)
        elif test_page == "ShipLinePage":
            return ShipLinePage(self.driver)
        elif test_page == "PortPage":
            return PortPage(self.driver)
        elif test_page == "SupCompanyPage":
            return SupCompanyPage(self.driver)
        elif test_page == "BuyCompanyPage":
            return BuyCompanyPage(self.driver)
        elif test_page == "SupEmpPage":
            return SupEmpPage(self.driver)
        elif test_page == "BuyEmpPage":
            return BuyEmpPage(self.driver)
        else:
            pass

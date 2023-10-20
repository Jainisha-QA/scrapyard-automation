import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Utils.BasePage import BasePage


class PayTermPage(BasePage):

    ADD_BTN = (By.XPATH, "//button[contains(text(),'Add')]")
    INPUT_TEXTBOX = (By.XPATH, "//input[@placeholder='Enter Payment Terms ']")
    TOAST_MSG = (By.ID, "toast-container")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")
    SEARCH_BOX = (By.XPATH, "//input[@placeholder='Search']")
    EDIT_BTN = (By.XPATH, "//td[3]/a[1]")
    DELETE_BTN = (By.XPATH, "//td[3]/a[2]")
    DATA_TBL_COLUMN = (By.XPATH, "//td[2]/container-element/container-element")
    CANCLE_BUTTON = (By.XPATH, "//button[contains(text(),'Cancel')]")
    REQUIRE_MSG = (By.XPATH, "//mat-error/span")

    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url == TestData.PAYTERMS_URL:
            pass
        else:
            self.driver.get(TestData.PAYTERMS_URL)

    def add_fun(self, value):
        self.do_click(self.ADD_BTN)
        self.do_send_keys(self.INPUT_TEXTBOX, value)
        self.do_click(self.SAVE_BTN)
        return self.get_text(self.TOAST_MSG)

    def search_fun(self, value):
        self.do_click(self.SEARCH_BOX)
        self.do_clear(self.SEARCH_BOX)
        self.do_send_keys(self.SEARCH_BOX, value)
        time.sleep(3)

    def update_fun(self, old_value, new_value):
        data = self.get_text(self.DATA_TBL_COLUMN)
        if data == old_value:
            self.do_click(self.EDIT_BTN)
            self.do_clear(self.INPUT_TEXTBOX)
            self.do_send_keys(self.INPUT_TEXTBOX, new_value)
            self.do_click(self.SAVE_BTN)
            return self.get_text(self.TOAST_MSG)
        else:
            return "Data not on First Row"

    def delete_fun(self, value):
        data = self.get_text(self.DATA_TBL_COLUMN)
        if data == value:
            self.do_click(self.DELETE_BTN)
            self.do_click(self.SAVE_BTN)
            return self.get_text(self.TOAST_MSG)
        else:
            return "Data not on First Row"

    def check_require_msg(self):
        self.do_click(self.ADD_BTN)
        self.do_send_keys(self.INPUT_TEXTBOX)
        msg = self.below_element_text(self.INPUT_TEXTBOX, self.REQUIRE_MSG[1])
        return msg

    def check_placeholder(self):
        placeholder = self.get_attribute_element(self.INPUT_TEXTBOX, "placeholder")
        self.do_click(self.CANCLE_BUTTON)
        return placeholder

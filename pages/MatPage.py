import time

from selenium.webdriver.common.by import By

from Config.config import TestData
from Utils.BasePage import BasePage


class MatPage(BasePage):

    ADD_BTN = (By.XPATH, "//button[contains(text(),'Add')]")
    DROP_DOWN = (By.XPATH, "//span[contains(text(),'Select Material Category')]")
    OPTION = (By.XPATH,"//span[contains(text(), 'MS Scrap')]" )
    INPUT_TEXTBOX1 = (By.XPATH, "//input[@placeholder='Enter material name']")
    INPUT_TEXTBOX2 = (By.XPATH, "//input[@placeholder='Enter Hs code']")
    TOAST_MSG = (By.ID, "toast-container")
    SAVE_BTN = (By.XPATH, "//button[@type='submit']")
    SEARCH_BOX = (By.XPATH, "//input[@placeholder='Search']")
    EDIT_BTN = (By.XPATH, "//td[5]/a[1]")
    DELETE_BTN = (By.XPATH, "//td[5]/a[2]")
    DATA_TBL_COLUMN = (By.XPATH, "//td[2]/container-element/container-element")
    CANCLE_BUTTON = (By.XPATH, "//button[contains(text(),'Cancel')]")
    REQUIRE_MSG = (By.XPATH, "//mat-error/span")

    def __init__(self, driver):
        super().__init__(driver)
        if self.driver.current_url == TestData.MAT_URL:
            pass
        else:
            self.driver.get(TestData.MAT_URL)

    def add_fun(self, value1, value2):
        self.do_click(self.ADD_BTN)
        self.do_click(self.DROP_DOWN)
        self.do_click(self.OPTION)
        self.do_send_keys(self.INPUT_TEXTBOX1, value1)
        self.do_send_keys(self.INPUT_TEXTBOX2, value2)
        self.do_click(self.SAVE_BTN)
        return self.get_text(self.TOAST_MSG)

    def search_fun(self, value):
        self.do_click(self.SEARCH_BOX)
        self.do_clear(self.SEARCH_BOX)
        self.do_send_keys(self.SEARCH_BOX, value)
        time.sleep(4)

    def update_fun(self, old_value, new_value):
        data = self.get_text(self.DATA_TBL_COLUMN)
        if data == old_value:
            self.do_click(self.EDIT_BTN)
            self.do_clear(self.INPUT_TEXTBOX1)
            self.do_send_keys(self.INPUT_TEXTBOX1, new_value[0])
            self.do_clear(self.INPUT_TEXTBOX2)
            self.do_send_keys(self.INPUT_TEXTBOX2, new_value[1])
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
        self.do_send_keys(self.INPUT_TEXTBOX1)
        self.do_send_keys(self.INPUT_TEXTBOX2)
        self.do_send_keys(self.INPUT_TEXTBOX1)
        msg0 = self.below_element_text(self.DROP_DOWN, self.REQUIRE_MSG[1])
        msg1 = self.below_element_text(self.INPUT_TEXTBOX1, self.REQUIRE_MSG[1])
        msg2 = self.below_element_text(self.INPUT_TEXTBOX2, self.REQUIRE_MSG[1])
        return msg0, msg1, msg2

    def check_placeholder(self):
        msg0 = self.get_attribute_element(self.INPUT_TEXTBOX1, "placeholder")
        msg1 = self.get_attribute_element(self.INPUT_TEXTBOX2, "placeholder")
        self.do_click(self.CANCLE_BUTTON)
        return msg0, msg1

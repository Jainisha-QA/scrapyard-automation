""" This file consider parents of all pages """
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

""" It contains generic class and utilities for all pages """


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def check_url(self, url):
        return WebDriverWait(self.driver, 10).until(ec.url_to_be(url))

    def do_click(self, by_locator):
        time.sleep(2)
        (WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator)).
         click())

    def do_send_keys(self, by_locator, text=""):
        if text == "" or text is None:
            (WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).
             send_keys(Keys.TAB))
        else:
            (WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).
                send_keys(text + Keys.TAB))


    def get_text(self, by_locator):
        element = (WebDriverWait(self.driver, 10, poll_frequency=1).
                   until(ec.element_to_be_clickable(by_locator)))
        return element.text

    def do_clear(self, by_locator):
        time.sleep(2)
        element = (WebDriverWait(self.driver, 10).
                   until(ec.visibility_of_element_located(by_locator)))
        element.clear()

    def get_attribute_element(self, by_locator, value):
        element = (WebDriverWait(self.driver, 10).
                   until(ec.visibility_of_element_located(by_locator)))
        return element.get_attribute(value)

    def is_visible(self, by_locator):
        element = (WebDriverWait(self.driver, 10).
                   until(ec.visibility_of_element_located(by_locator)))
        return bool(element)

    def is_enable(self, by_locator):
        element = (WebDriverWait(self.driver, 10).
                   until(ec.visibility_of_element_located(by_locator)))
        return element.is_enabled()

    def is_display(self, by_locator):
        element = (WebDriverWait(self.driver, 10).
                   until(ec.visibility_of(by_locator)))
        return element.is_displayed()

    def get_title(self, title):
        (WebDriverWait(self.driver, 10).
         until(ec.title_is(title)))
        return self.driver.title

    def get_element_border_color(self, by_locator):
        element = (WebDriverWait(self.driver, 10).
                   until((ec.visibility_of_element_located(by_locator))))
        s = element.value_of_css_property("color")
        c = Color.from_string(s).hex
        return c

    def get_screenshot(self, imagepath):
        self.driver.get_screenshot_as_file(imagepath)

    def access_localstorage(self):
        return self.driver.execute_script("return windows.localStorage")

    def below_element_text(self, by_locator1, by_locator2):
        element = (WebDriverWait(self.driver, 10).
                   until((ec.visibility_of_element_located(by_locator1))))
        require_msg = self.driver.find_element(locate_with(By.XPATH, by_locator2).
                                           below(element))
        return require_msg.text

    def action_click(self, by_locator):
        element = (WebDriverWait(self.driver, 10).
                   until((ec.element_to_be_clickable(by_locator))))
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()

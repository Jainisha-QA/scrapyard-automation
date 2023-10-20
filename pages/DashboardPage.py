import os
import time

from selenium.webdriver.common.by import By
from Utils.BasePage import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def check_full_screen(self, filename):
        dir_name = os.path.normpath(os.getcwd())
        # print(dir_name)
        outputDirectory = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'images').replace("python", ""))
        # print(outputDirectory)
        filename = outputDirectory + filename
        # print(filename)
        if self.driver.execute_script('return document.readyState') == 'complete':
            pass
        else:
            time.sleep(10)
        self.get_screenshot(filename)


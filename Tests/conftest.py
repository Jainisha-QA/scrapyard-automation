import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(params=["Chrome"], scope='class')
def init_driver(request):
    # web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    web_driver = webdriver.Chrome(executable_path="https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/")
    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    yield
    # print(web_driver.current_url)
    web_driver.close()
    web_driver.quit()

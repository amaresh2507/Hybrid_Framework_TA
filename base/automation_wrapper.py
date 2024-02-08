import pytest
from selenium import webdriver
import logging

import config
from utils import read_utils

"""Code helps to configure browser for all test methods"""
Logger = logging.getLogger()


class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # runs before each test_method
        self.json_config = read_utils.get_json_as_dic(json_location=config.test_data_path + r"\config.json")
        browser = self.json_config["browser"]
        if browser == "edge":
            self.driver = webdriver.Edge()
        elif browser == "ff":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.json_config["url"])
        Logger.info(f"Launched browser {browser} and navigated to {self.json_config['url']}")
        yield
        # runs after each testt_method
        self.driver.quit()
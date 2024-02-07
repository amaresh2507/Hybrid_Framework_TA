import time

import pytest
from selenium import webdriver


class WebDriverWrapper():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        browser = 'edge'
        if browser == 'edge':
            self.driver = webdriver.Edge()
        elif browser == 'ff':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://demo.openemr.io/b/openemr/")

        yield
        time.sleep(5)
        self.driver.quit()

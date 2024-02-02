import time

import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLogin:

    @pytest.fixture(scope="function",autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://demo.openemr.io/b/openemr/")
        yield
        time.sleep(5)
        self.driver.quit()

    def test_Title(self):

        title_page = self.driver.title
        # assert title_page == "OpenEMR Login"
        assert_that(title_page).is_equal_to("OpenEMR Logins")
        print(title_page)

    def test_Desc(self):

        text = self.driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
        assert_that(text).contains("Electronic Health Record and Medical Practice Management")
        self.driver.quit()

#master branch pushed
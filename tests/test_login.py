import time

import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class WebDriverWrapper():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("http://demo.openemr.io/b/openemr/")

        yield
        time.sleep(5)
        self.driver.quit()


class TestLogin(WebDriverWrapper):

    def test_Title(self):
        title_page = self.driver.title
        # assert title_page == "OpenEMR Login"
        assert_that(title_page).is_equal_to("OpenEMR Logins")
        print(title_page)

    def test_Desc(self):
        text = self.driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
        assert_that(text).contains("Electronic Health Record and Medical Practice Management")

    def test_Placeholder_Usr(self):
        placeholder_usr = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").get_attribute('placeholder')
        print(placeholder_usr)
        assert_that(placeholder_usr).is_equal_to('Username')

    def test_Placeholder_Pwd(self):
        placeholder_pwd = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").get_attribute('placeholder')
        print(placeholder_pwd)
        assert_that(placeholder_pwd).is_equal_to('Passwords')

# master branch pushed

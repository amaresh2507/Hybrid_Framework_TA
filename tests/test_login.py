import time

import pytest
import pytest_html
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.automation_wrapper import WebDriverWrapper
from utils.data_utils import DataSource


class TestLogin(WebDriverWrapper):
    @pytest.mark.parametrize(
        "username, password, expect_title",
        DataSource.data_valid
    )
    def test_valid_login(self, username, password, expect_title):
        self.driver.find_element(By.ID, "authUser").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert_that(expect_title).is_equal_to(self.driver.title)

    @pytest.mark.parametrize(
        "username, password, error_msg",
        DataSource.data_invalid
    )
    def test_invalid_login(self, username, password, error_msg):
        self.driver.find_element(By.ID, "authUser").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        err_msg = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Invalid')]").text
        assert_that(err_msg).contains(error_msg)

    def test_Title(self):
        title_page = self.driver.title
        # assert title_page == "OpenEMR Login"
        assert_that(title_page).is_equal_to("OpenEMR Login")
        print(title_page)

    def test_Desc(self):
        text = self.driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
        assert_that(text).contains("Electronic Health Record and Medical Practice Management")

    def test_Placeholder_Usr(self):
        placeholder_usr = self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").get_attribute(
            'placeholder')
        print(placeholder_usr)
        assert_that(placeholder_usr).is_equal_to('Username')

    def test_Placeholder_Pwd(self):
        placeholder_pwd = self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").get_attribute(
            'placeholder')
        print(placeholder_pwd)
        assert_that(placeholder_pwd).is_equal_to('Passwords')

# master branch pushed

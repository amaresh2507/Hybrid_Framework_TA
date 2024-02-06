import time

import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By
from base.automation_wrapper import WebDriverWrapper
from utils.data_utils import DataSource
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLogin(WebDriverWrapper):
    @pytest.mark.parametrize(
        "username, password, expect_title",
        DataSource.data_valid
    )
    def test_valid_login(self, username, password, expect_title):
        login = LoginPage(self.driver)
        login.login_username(username)
        login.login_password(password)
        login.login_button()
        assert_that(expect_title).is_equal_to(self.driver.title)

    @pytest.mark.parametrize(
        "username, password, error_msg",
        DataSource.data_invalid
    )
    def test_invalid_login(self, username, password, error_msg):
        login = LoginPage(self.driver)
        login.login_username(username)
        login.login_password(password)
        login.login_button()
        err_msg = login.error_message()
        assert_that(err_msg).contains(error_msg)

    def test_Title(self):
        main_pg = MainPage(self.driver)
        title_page = main_pg.get_main_title
        assert_that(title_page).is_equal_to("OpenEMR Login")

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

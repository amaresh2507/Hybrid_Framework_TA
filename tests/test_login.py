import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import WebDriverWrapper, Logger
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.data_utils import DataSource


class TestLogin(WebDriverWrapper):

    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.valid
    @pytest.mark.parametrize("username,password,expected_title", DataSource.data_valid_login_excel)
    def test_valid_login(self, username, password, expected_title):
        login = LoginPage(self.driver)
        login.enter_username(username)
        Logger.info(f"Entered username as {username}")
        login.enter_password(password)
        Logger.info(f"Entered password as {password}")
        login.click_on_login()
        Logger.info(f"Clicked on login")
        main = MainPage(self.driver)
        Logger.info(f"Actual title {main.get_main_title}")
        assert_that(expected_title).is_equal_to(main.get_main_title)
        Logger.info(f"Test Passed for {username}")

    @pytest.mark.login
    @pytest.mark.parametrize("username,password,expected_error", DataSource.data_invalid_login_excel)
    def test_invalid_login(self, username, password, expected_error):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_on_login()
        actual_error = login.get_error_message()
        assert_that(actual_error).contains(expected_error)


class TestLoginUI(WebDriverWrapper):
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_title(self):
        login = LoginPage(self.driver)
        assert_that("OpenEMR Login").is_equal_to(login.get_login_title)

    @pytest.mark.ui
    def test_app_description(self):
        login = LoginPage(self.driver)
        # actual_desc = login.get_app_desc
        assert_that(login.get_app_desc).contains("Electronic Health Record and Medical Practice Management")

    @pytest.mark.ui
    def test_placeholder(self):
        login = LoginPage(self.driver)
        assert_that("Username").is_equal_to(login.get_username_placeholder)
        assert_that("Password").is_equal_to(login.get_password_placeholder)
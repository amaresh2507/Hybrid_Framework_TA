import time

from selenium.webdriver.common.by import By

from base.automation_wrapper import WebDriverWrapper
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.search_add_page import SearchOrAddPatientPage



class TestAddPatient(WebDriverWrapper):
    def test_add_valid_patient_test(self):
        login = LoginPage(self.driver)
        login.enter_username("admin")
        login.enter_password("pass")
        login.click_on_login()

        main=MainPage(self.driver)
        main.click_on_patient_menu()
        main.click_on_new_search_menu()

        search=SearchOrAddPatientPage(self.driver)
        search.enter_firstname("john")
        self.driver.find_element(By.Id,"form_lname").send_keys("wick")
        #complete as per the task given on day 3c
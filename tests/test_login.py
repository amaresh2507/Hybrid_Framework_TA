import time

from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLogin:
    def test_Title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("http://demo.openemr.io/b/openemr/")
        title_page = driver.title
        # assert title_page == "OpenEMR Login"
        assert_that(title_page).is_equal_to("OpenEMR Logins")
        print(title_page)
        time.sleep(5)

    def test_Desc(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("http://demo.openemr.io/b/openemr/")
        text = driver.find_element(By.XPATH, "//p[@class='text-center lead']").text
        assert_that(text).contains("Electronic Health Record and Medical Practice Management")
        time.sleep(5)
        driver.quit()

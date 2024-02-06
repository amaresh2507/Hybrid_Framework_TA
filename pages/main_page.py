from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class MainPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__patient_locator=(By.XPATH, "//div[text()='Patient']")
        self.__new_search_locator=(By.XPATH, "//div[text()='New/Search']")

    @property
    def get_main_title(self):
        return self.__driver.title

    def click_on_patient_menu(self):
        # self.__driver.find_element(By.XPATH, "//div[text()='Patient']").click()
        super().click_on_element(self.__patient_locator)

    def click_on_new_search_menu(self):
        # self.__driver.find_element(By.XPATH, "//div[text()='New/Search']").click()
        super().click_on_element(self.__new_search_locator)
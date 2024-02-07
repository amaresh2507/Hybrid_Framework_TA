from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class SearchOrAddPatientPage(WebDriverKeywords):
    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__firstname_locator=(By.Id,"form_fname")

    def enter_firstname(self,first_name):
        self.__driver.switch_to.frame(self.driver.find_element(By.NAME,"pat"))
        super().type_on_element(self.__firstname_locator,first_name)
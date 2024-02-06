from selenium.webdriver.common.by import By


class MainPage:

    def __init__(self, driver):
        self.__driver = driver

    @property
    def get_main_title(self):
        return self.__driver.title

    def click_on_patient_menu(self):
        self.__driver.find_element(By.XPATH, "//div[text()='Patient']").click()

    def click_on_new_search_menu(self):
        self.__driver.find_element(By.XPATH, "//div[text()='New/Search']").click()

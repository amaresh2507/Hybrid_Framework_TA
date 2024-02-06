from selenium.webdriver.common.by import By

from base.webdriver_keywords import WebDriverKeywords


class LoginPage(WebDriverKeywords):

    def __init__(self, driver):
        super().__init__(driver)
        self.__driver = driver
        self.__username_locator = (By.ID, "authUser")
        self.__password_locator = (By.CSS_SELECTOR, "#clearPass")
        self.__login_locator = (By.ID, "login-button")
        self.__invalid_error_locator = (By.XPATH, "//p[contains(text(),'Invalid')]")
        self.__app_desc_locator = (By.XPATH, "//p[contains(text(),'most')]")

    def enter_username(self, username):
        # self.__driver.find_element(By.ID, "authUser").send_keys(username)
        super().type_on_element(self.__username_locator, username)

    def enter_password(self, password):
        # self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)
        super().type_on_element(self.__password_locator, password)

    def click_on_login(self):
        # self.__driver.find_element(By.ID, "login-button").click()
        super().click_on_element(self.__login_locator)

    def get_error_message(self):
        # return self.__driver.find_element(By.XPATH, "//p[contains(text(),'Invalid')]").text
        return super().get_text_from_element(self.__invalid_error_locator)

    @property
    def get_login_title(self):
        return self.__driver.title

    @property
    def get_app_desc(self):
        # return self.__driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        return super().get_text_from_element(self.__app_desc_locator)

    @property
    def get_username_placeholder(self):
        # return self.__driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        return super().get_attribute_from_element(self.__username_locator, "placeholder")

    @property
    def get_password_placeholder(self):
        # return self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").get_attribute("placeholder")
        return super().get_attribute_from_element(self.__password_locator, "placeholder")
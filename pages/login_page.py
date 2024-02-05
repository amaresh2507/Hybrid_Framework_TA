from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.__driver = driver

    def login_username(self, username):
        self.__driver.find_element(By.ID, "authUser").send_keys(username)

    def login_password(self, password):
        self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)

    def login_button(self):
        self.__driver.find_element(By.ID, "login-button").click()

    def error_message(self):
        err_msg = self.__driver.find_element(By.XPATH, "//p[contains(text(), 'Invalid')]").text
        return  err_msg
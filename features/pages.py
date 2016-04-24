from selenium.webdriver.common.by import By


class LoginPage:
    USER_INPUT = (By.ID, 'user_login')
    PASSWORD_INPUT = (By.ID, 'user_pass')
    SUBMIT_INPUT = (By.ID, 'wp-submit')
    ERROR_DIV = (By.ID, 'login_error')

    def __init__(self, driver):
        self.driver = driver

    def login_with_credential(self, user, password):
        self.driver.find_element(*self.USER_INPUT).send_keys(user)
        if password != "N/A":
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SUBMIT_INPUT).click()

    def get_login_error(self):
        return self.driver.find_element(*self.ERROR_DIV).text

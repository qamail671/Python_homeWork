from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )

        login_button.click()

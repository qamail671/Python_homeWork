from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver):
        """
        Инициализация LoginPage.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Заполняет поле 'Username' на странице авторизации.

        Args:
            username (str): Имя пользователя для авторизации
        """
        username_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_field.send_keys(username)

    @allure.step("Ввести пароль ")
    def enter_password(self, password: str) -> None:
        """
        Заполняет поле 'Password' на странице авторизации.

        Args:
            password (str): Пароль пользователя для авторизации
        """
        password_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(password)

    @allure.step("Нажать кнопку 'Login'")
    def click_login(self) -> None:
        """Нажимает кнопку 'Login' для выполнения авторизации."""
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()
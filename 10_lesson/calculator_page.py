from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class CalculatorPage:
    """Класс для работы со страницей калькулятора с задержкой."""

    def __init__(self, driver):
        """
        Инициализация CalculatorPage.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы элементов
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CLASS_NAME, "screen")

    @allure.step("Установить задержку вычислений: {seconds} секунд")
    def set_delay(self, seconds: str) -> None:
        """
        Вводит значение задержки в поле ввода.

        Args:
            seconds (str): Количество секунд задержки вычислений
        """
        delay_input = self.wait.until(EC.element_to_be_clickable(
            self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(seconds)

    @allure.step("Нажать кнопку '7'")
    def click_button_7(self) -> None:
        """Нажимает кнопку '7' на калькуляторе."""
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_7))
        button.click()

    @allure.step("Нажать кнопку '+'")
    def click_button_plus(self) -> None:
        """Нажимает кнопку сложения '+' на калькуляторе."""
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_PLUS))
        button.click()

    @allure.step("Нажать кнопку '8'")
    def click_button_8(self) -> None:
        """Нажимает кнопку '8' на калькуляторе."""
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_8))
        button.click()

    @allure.step("Нажать кнопку '='")
    def click_equals(self) -> None:
        """Нажимает кнопку равенства '=' для выполнения вычислений."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUALS))
        button.click()

    @allure.step("Получить результат вычислений")
    def get_result(self) -> str:
        """
        Получает текст из поля результата вычислений.

        Returns:
            str: Текст результата вычислений
        """
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_SCREEN))
        return result_element.text
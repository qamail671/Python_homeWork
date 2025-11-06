
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локаторы элементов
    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CSS_SELECTOR, "div.screen")

    def set_delay(self, seconds: str):
        """Вводит значение задержки в поле ввода."""
        delay_input = self.wait.until(EC.element_to_be_clickable(
            self.DELAY_INPUT))
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button_7(self):
        """Нажимает кнопку '7'."""
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_7))
        button.click()

    def click_button_plus(self):
        """Нажимает кнопку '+'."""
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_PLUS))
        button.click()

    def click_button_8(self):
        """Нажимает кнопку '8'."""
        button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_8))
        button.click()

    def click_equals(self):
        """Нажимает кнопку '='."""
        button = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_EQUALS))
        button.click()

    def get_result(self) -> str:
        """Получает текст из поля результата."""
        result_element = self.wait.until(
            EC.visibility_of_element_located(self.RESULT_SCREEN))
        return result_element.text

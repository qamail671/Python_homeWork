from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver):
        """
        Инициализация CheckoutPage.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить поле 'Имя' значением: {first_name}")
    def fill_first_name(self, first_name: str) -> None:
        """
        Заполняет поле 'First Name' в форме оформления заказа.

        Args:
            first_name (str): Имя покупателя
        """
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(first_name)

    @allure.step("Заполнить поле 'Фамилия' значением: {last_name}")
    def fill_last_name(self, last_name: str) -> None:
        """
        Заполняет поле 'Last Name' в форме оформления заказа.

        Args:
            last_name (str): Фамилия покупателя
        """
        last_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        last_name_field.send_keys(last_name)

    @allure.step("Заполнить поле 'Почтовый индекс' значением: {postal_code}")
    def fill_postal_code(self, postal_code: str) -> None:
        """
        Заполняет поле 'Postal Code' в форме оформления заказа.

        Args:
            postal_code (str): Почтовый индекс покупателя
        """
        postal_code_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        )
        postal_code_field.send_keys(postal_code)

    @allure.step("Нажать кнопку 'Continue'")
    def click_continue(self) -> None:
        """Нажимает кнопку 'Continue' для перехода к подтверждению заказа."""
        continue_button = self.driver.find_element(
            By.CSS_SELECTOR, "#continue")
        continue_button.click()

    @allure.step("Получить итоговую сумму заказа")
    def get_total_price(self) -> float:
        """
        Получает итоговую сумму заказа со страницы подтверждения.

        Returns:
            float: Итоговая сумма заказа
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[data-test="total-label"]'))
        )

        total_text = total_element.text
        # Извлекаем число из строки вида "Total: $58.29"
        total_str = total_text.split()[-1].replace('$', '')
        return float(total_str)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver):
        """
        Инициализация CartPage.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self) -> None:
        """Нажимает кнопку 'Checkout' для перехода к оформлению заказа."""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

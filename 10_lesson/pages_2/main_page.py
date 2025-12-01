from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """Класс для работы с главной страницей интернет-магазина."""

    def __init__(self, driver):
        """
        Инициализация MainPage.

        Args:
            driver: WebDriver instance для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить рюкзак в корзину")
    def add_backpack_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Backpack' в корзину."""
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[text()='Add to cart' and contains(@id, 'backpack')]")
                                       )
        )
        add_button.click()

    @allure.step("Добавить футболку Bolt в корзину")
    def add_bolt_tshirt_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Bolt T-Shirt' в корзину."""
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[text()='Add to cart' and contains(@id, 't-shirt')]")
            )
        )
        add_button.click()

    @allure.step("Добавить комбинезон в корзину")
    def add_onesie_to_cart(self) -> None:
        """Добавляет товар 'Sauce Labs Onesie' в корзину."""
        add_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[text()='Add to cart' and contains(@id, 'onesie')]")
            )
        )
        add_button.click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Переходит на страницу корзины."""
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()

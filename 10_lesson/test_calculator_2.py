import pytest
import allure
from selenium.webdriver.chrome.service import Service
from calculator_page import CalculatorPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для управления WebDriver.

    Yields:
        WebDriver instance
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.NORMAL)
class TestCalculator:
    """Тестовый класс для проверки калькулятора с задержкой вычислений."""

    @allure.title("Проверка сложения с задержкой 45 секунд")
    @allure.description(
        "Этот тест проверяет работу калькулятора с установленной задержкой."
        "1. Установка задержки 45 секунд."
        "2. Выполнение операции 7 + 8."
        "3. Ожидание результата в течение 47 секунд."
        "4. Проверка корректности результата (15)."
    )
    @allure.tag("calculator", "slow", "addition")
    def test_calculator_addition(self, driver):
        """
        Тест: проверка сложения 7 + 8 с задержкой 45 секунд.
        Ожидаемый результат: 15
        """
        with allure.step("Открыть страницу калькулятора с задержкой"):
            driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
            )

        # Создаем объект страницы
        calculator = CalculatorPage(driver)

        with allure.step("Установить задержку вычислений 45 секунд"):
            calculator.set_delay("45")

        with allure.step("Выполнить операцию сложения: 7 + 8"):
            calculator.click_button_7()
            calculator.click_button_plus()
            calculator.click_button_8()
            calculator.click_equals()

        with allure.step("Ожидать результат вычислений (47 секунд)"):
            wait = WebDriverWait(driver, 60)  # Создаём объект ожидания
            wait.until(
                EC.text_to_be_present_in_element(
                    (calculator.RESULT_SCREEN), "15"
                )  # Передаем правильный локатор By.ID и ID-элемент
            )

        with allure.step("Проверить результат вычислений"):
            result = calculator.get_result()

        with allure.step("Убедиться, что результат равен 15"):
            assert result == "15", f"Ожидаемый результат '15', но получен '{result}'"

    @allure.step("Дополнительная проверка: убедиться, что результат не пустой")
    def _verify_result_not_empty(self, result: str) -> None:
        """
        Вспомогательный метод для проверки, что результат не пустой.

        Args:
            result (str): Результат вычислений для проверки
        """

        assert result != "", "Результат вычислений не должен быть пустым"
        assert result is not None, "Результат вычислений не должен быть None"

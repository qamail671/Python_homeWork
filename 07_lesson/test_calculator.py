import pytest
from selenium.webdriver.chrome.service import Service
from calculator_page import CalculatorPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """Фикстура для управления WebDriver."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator_addition(driver):
    """
    Тест: проверка сложения 7 + 8 с задержкой 45 секунд.
    Ожидаемый результат: 15
    """
    # Открываем страницу калькулятора
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Создаем объект страницы
    calculator = CalculatorPage(driver)

    # Шаг 1: Вводим значение задержки 45 секунд
    calculator.set_delay("45")

    # Шаг 2: Выполняем вычисления: 7 + 8 =
    calculator.click_button_7()
    calculator.click_button_plus()
    calculator.click_button_8()
    calculator.click_equals()

    # Шаг 3: Ожидаем результат (45 секунд + запас на загрузку)
    import time
    time.sleep(46)  # 46 секунд

    # Шаг 4: Проверяем результат
    result = calculator.get_result()
    assert result == "15", f"Ожидаемый результат '15', но получен '{result}'"

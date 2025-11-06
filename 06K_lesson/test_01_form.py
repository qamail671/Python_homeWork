
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service as EdgeService

# Импортируем необходимые библиотеки




# Объявляем тестовую функцию
def test_fill_form():
    # Устанавливаем драйвер для браузера Edge или Safari
    driver = webdriver.Edge()  # или webdriver.Safari()

    driver.fullscreen_window()
    try:
        # Шаг 1: Открываем нужную страницу
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

        # Шаг 2: Заполняем форму
        driver.find_element(By.NAME, 'first-name').send_keys('Иван')
        driver.find_element(By.NAME, 'last-name').send_keys('Петров')
        driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
        driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
        driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
        driver.find_element(By.NAME, 'job-position').send_keys('QA')
        driver.find_element(By.NAME, 'company').send_keys('SkyPro')
        driver.find_element(By.NAME, 'city').send_keys('Москва')
        driver.find_element(By.NAME, 'country').send_keys('Россия')

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        #Нажимаем кнопку Submit
        driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

        waiter = WebDriverWait(driver, 10)
        waiter.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#zip-code'))
        )
        # Шаг 4: Проверяем подсветку полей
        zip_code_field = driver.find_element(By.CSS_SELECTOR, "#zip-code")
        assert "alert-danger" in zip_code_field.get_attribute('class')
        # Проверка остальных полей на зеленую подсветку
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'job-position','company', 'city', 'country' ]
        for locator in fields:
            field = driver.find_element(By.ID, locator )
            assert "alert-success" in field.get_attribute('class')

    finally:
        # Закрываем браузер
        driver.quit()
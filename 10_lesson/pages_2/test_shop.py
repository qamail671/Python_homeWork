import allure
import pytest
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
class TestShop:

    @allure.title("Проверка покупки товаров с итоговой суммой $58.29")
    @allure.description(
        "Тест проверяет полный процесс покупки: авторизация,"
        " добавление 3 товаров, оформление заказа и проверка суммы")
    @allure.feature("Покупка товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_purchase_items(self, driver):
        with allure.step("Открыть сайт SauceDemo"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Авторизоваться на сайте"):
            login_page = LoginPage(driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавить товары в корзину"):
            main_page = MainPage(driver)
            main_page.add_backpack_to_cart()
            main_page.add_bolt_tshirt_to_cart()
            main_page.add_onesie_to_cart()

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        with allure.step("Нажать Checkout"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Заполнить форму оформления заказа"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_first_name("Евгений")
            checkout_page.fill_last_name("Саханевич")
            checkout_page.fill_postal_code("456020")
            checkout_page.click_continue()

        with allure.step("Получить итоговую сумму"):
            total = checkout_page.get_total_price()

        with allure.step("Проверить итоговую сумму"):
            expected_total = 58.29
            assert total == expected_total, (f"Expected total"
                                     f" ${expected_total}, but got ${total}")
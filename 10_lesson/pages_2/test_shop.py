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
    def test_purchase_items(self, driver):
        # Шаг 1: Открыть сайт
        driver.get("https://www.saucedemo.com/")

        # Шаг 2: Авторизоваться
        login_page = LoginPage(driver)
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Шаг 3: Добавить товары в корзину
        main_page = MainPage(driver)
        main_page.add_backpack_to_cart()
        main_page.add_bolt_tshirt_to_cart()
        main_page.add_onesie_to_cart()

        # Шаг 4: Перейти в корзину
        main_page.go_to_cart()

        # Шаг 5: Нажать Checkout
        cart_page = CartPage(driver)
        cart_page.click_checkout()

        # Шаг 6: Заполнить форму
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_first_name("Евгений")
        checkout_page.fill_last_name("Саханевич")
        checkout_page.fill_postal_code("456020")
        checkout_page.click_continue()

        # Шаг 7: Получить итоговую сумму
        total = checkout_page.get_total_price()

        # Шаг 8: Проверить итоговую сумму
        expected_total = 58.29
        assert total == expected_total, \
            f" Expected total ${expected_total}, but got ${total} "

        driver.quit()

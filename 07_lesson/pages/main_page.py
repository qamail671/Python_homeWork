from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
            "//button[text()='Add to cart' and contains(@id, 'backpack')]")
            )
        )
        add_button.click()

    def add_bolt_tshirt_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(
            (By.XPATH,
             "//button[text()='Add to cart' and contains(@id, 't-shirt')]")
            )
        )
        add_button.click()

    def add_onesie_to_cart(self):
        add_button = self.wait.until(
            EC.element_to_be_clickable(
            (By.XPATH,
                "//button[text()='Add to cart' and contains(@id, 'onesie')]")
            )
        )
        add_button.click()

    def go_to_cart(self):
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_first_name(self, first_name):
        first_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_field.send_keys(first_name)

    def fill_last_name(self, last_name):
        last_name_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        last_name_field.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        postal_code_field = self.wait.until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        )
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.driver.find_element(
            By.CSS_SELECTOR, "#continue")
        continue_button.click()

    def get_total_price(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'div[data-test="total-label"]'))
        )

        total_text = total_element.text
        # Извлекаем число из строки вида "Total: $58.29"
        total_str = total_text.split()[-1].replace('$', '')
        return float(total_str)

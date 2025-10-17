
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

element = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

element.send_keys("Sky")

element.clear()

element.send_keys("Pro")

driver.quit()

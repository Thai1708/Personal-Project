import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.implicitly_wait(5)

sum1 = driver.find_element(By.ID, "value1")
sum2 = driver.find_element(By.ID, "value2")
# Thay vi go truc tiep, dung key cua ban phim
sum1.send_keys(Keys.NUMPAD1, Keys.NUMPAD2)
sum2.send_keys(12)

total_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick = "return total()"]')
total_button.click()
time.sleep(20)
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

driver.implicitly_wait(10)
my_element = driver.find_element(By.ID, "downloadButton")
my_element.click()

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'progress-label'),
        'Complete!'
    )
)
progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print(f"{progress_element.text}")

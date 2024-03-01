# with open('data_carreerbuilder.txt', 'r', encoding='utf8') as file:
#     data = file.read()

# list_data = data.split("#")
# for i in range(len(list_data)):
#     print(list_data)
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from time import sleep
import random

import pandas as pd
import numpy as np

# Declare browser

os.environ['PATH'] += r"C:/SeleniumDrivers"
# Khởi tạo trình duyệt Chrome
options = uc.ChromeOptions()

# Tắt notifications
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)

# Khởi tạo trình duyệt với các tùy chọn đã thiết lập
driver = uc.Chrome(options=options)
# driver = webdriver.Chrome()

# Open URL
driver.maximize_window()
driver.implicitly_wait(2)

driver.get('https://careerbuilder.vn/vi/tim-viec-lam/senior-marketing-executive-parfois.35BF2AB8.html')


yeu_cau = driver.find_element(By.XPATH, '//*[@id="tab-1"]/section/div[4]')
print(yeu_cau.text)

# khac_element = driver.find_element(By.XPATH, '//*[@id="tab-1"]/section/div[5]/div')
# # khac = khac_element.text
# print(khac_element.text)

sleep(10)
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
driver.implicitly_wait(3)
# link_ = 'https://careerbuilder.vn/viec-lam/tiep-thi-marketing-c4-trang-1-vi.html'
link_pages = []
for i in range(1, 34):
    link_pages.append(f'https://vieclam24h.vn/mien-nam/viec-lam-marketing-o12.html?occupation_ids%5B%5D=12&page={i}&sort_q=')
# link detailed page
number_link_each_pages = {}
for i in range(len(link_pages)):
    links = []
    print(f"DANG O TRANG {i+1}***********************************")
    driver.get(link_pages[i])
    sleep(1.5)

    link_elements = driver.find_elements(By.XPATH, '//div[@class="relative w-full border hover:shadow-md rounded-sm lg:rounded-none bg-white border-se-blue-10"]/a[1]')
    print(len(link_elements))
    if len(link_elements) == 0:
        print("Khong tim duoc link, can kiem tra lai")
    
    number_link_each_pages[f"{i+1}"] = (len(link_elements))

    for l in link_elements:
        links.append(l.get_attribute('href'))
        print(l.get_attribute('href'))
    with open('link_subpage_vieclam24h.txt', 'a') as file:
        for l in links:
            file.write(l + '\n')
print(number_link_each_pages)

sleep(10)











# link_elements = driver.find_elements(By.XPATH, '//div[@class="relative w-full border hover:shadow-md rounded-sm lg:rounded-none bg-white border-se-blue-10"]/a[1]')
# print(len(link_elements))
# for i in range(len(link_elements)):
#     print(link_elements[i].get_attribute('href'))

sleep(10)
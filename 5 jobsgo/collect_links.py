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
# driver.implicitly_wait(3)
# link_ = 'https://careerbuilder.vn/viec-lam/tiep-thi-marketing-c4-trang-1-vi.html'
link_pages = []
for i in range(1, 17):
    link_pages.append(f'https://jobsgo.vn/viec-lam-marketing.html?page={i}')
# link detailed page
links = []
for link_ in link_pages:
    driver.get(link_)
    sleep(1)

    link_elements = driver.find_elements(By.XPATH, '//h3[@class="h3 tooltip tooltipstered"]//a[@target="_blank"]')
    for l in link_elements:
        links.append(l.get_attribute('href'))
    print("===================================================")
    print(len(link_elements))
    print(len(links))
    print(links)

    print("===================================================")

print("###############################################")
with open('link_subpage_jobsgo.txt', 'a') as file:
    for l in links:
        file.write(l + '\n')
print("###############################################")

sleep(10)
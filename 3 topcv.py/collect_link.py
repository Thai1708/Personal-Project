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

# driver.get('https://www.topcv.vn/tim-viec-lam-marketing-truyen-thong-quang-cao-c10029?sort=top_related')

link_pages = []
for i in range(1, 208):
    link_pages.append(f'https://www.topcv.vn/tim-viec-lam-marketing-truyen-thong-quang-cao-c10029?sort=top_related&page={i}')
# link detailed page

for i in range(len(link_pages)):
    print("*******************************************************************")
    print(f"DANG O TRANG {i+1}")
    links = []
    driver.get(link_pages[i])

    sleep(1)
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, '#popup-survey-recruitment-trend > div > div > div.modal-header > button')
        close_button.click()
    except Exception as e:
        print(f"PAGE {i+1} khong co quang cao")
    sleep(0.5)

    link_elements = driver.find_elements(By.XPATH, '//h3[@class="title"]//a[@target="_blank"]')
    for l in link_elements:
        links.append(l.get_attribute('href'))
    print("===================================================")
    print(len(link_elements))
    print(len(links))
    print(links)
    print("===================================================")
    
    # for link in links:
    #     with open("link_subpage_topcv.txt", "a") as file:
    #         file.write(link + '\n')

sleep(100)

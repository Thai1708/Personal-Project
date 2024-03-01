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


class Information:
    def __init__(self, titles, companys, salarys, locations, dates, caps, nganh_nghes, ky_nangs, links):
        self.titles = titles
        self.companys = companys
        self.salarys = salarys
        self.locations = locations
        self.dates = dates
        self.caps = caps
        self.nganh_nghes = nganh_nghes
        self.ky_nangs = ky_nangs
        self.links = links

#-----------------------------------------------Link pages-----------------------------------------------

driver.get('https://www.vietnamworks.com/nghien-cuu-phan-tich-thi-truong-kv')
# driver.get("https://www.vietnamworks.com/chuyen-vien-marketing-805--1725696-jv?source=searchResults&searchType=2&placement=1725696&sortBy=date")

# Option 1:
pre_height = driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
count = 1
while True:
    print('-----scroll: {} times-----'.format(count))
    
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(3)
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    print('new_height: {}\npre_height: {}'.format(new_height, pre_height))

    if new_height == pre_height:
        print("While loop Done!!!")
        break
    
    count += 1
    pre_height = new_height    

links = []
link_elements = driver.find_elements(By.XPATH, '//div[@class="sc-kWtpeL kLqfwh"]//a[@target="_blank"]')
print(len(link_elements))
for t in link_elements:
    links.append(t.get_attribute('href'))
    print(t.get_attribute('href'))

with open('link_nghiencuuvaphantichthitruong.txt', 'a') as file:
    for link in links:
        file.write(link + '\n')
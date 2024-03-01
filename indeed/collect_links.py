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

driver.get('https://vn.indeed.com/jobs?q=marketing&l=&from=searchOnHP&vjk=c519b9668f25e641')
sleep(3)

try:
    close_button = driver.find_element(By.CSS_SELECTOR, '#mosaic-desktopserpjapopup > div.css-g6agtu.eu4oa1w0 > button')
    close_button.click()
except Exception as e:
    print("Close the pop up")
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
sleep()

link_page = driver.find_element(By.CSS_SELECTOR, '#jobsearch-JapanPage > div > div.css-h24f6n.eu4oa1w0 > a')
print(link_page.get_attribute('href'))
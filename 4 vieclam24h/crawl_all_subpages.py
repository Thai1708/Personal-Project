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

class Information:
    def __init__(self, title, company, salary, location, date, block_infor, yeu_cau , link):
        self.title = title
        self.company = company
        self.salary = salary
        self.location = location
        self.date = date
        self.block_infor = block_infor
        self.yeu_cau = yeu_cau
        self.link = link
#--------------------------------------Tao bien link tat ca trang-------------------------------------
with open('bad_links1_vieclam24h.txt', 'r', encoding='utf8') as file:
    link_pages = file.read().splitlines()

print(link_pages)

#--------------------------------------Crawl all page-------------------------------------------------
for i in range(len(link_pages)):
    print('DANG O TRANG ', str(i+1))
    sleep(3)
    driver.get(link_pages[i])
    sleep(0.25)

    try:
        title_element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div.md\:px-10.py-3.md\:py-4.px-4.bg-white.shadow-sd-12.rounded-sm.mb-5 > div.md\:flex.w-full.items-start > div > h1')
        title = title_element.text
        print(title)

        company_element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div.md\:px-10.py-3.md\:py-4.px-4.bg-white.shadow-sd-12.rounded-sm.mb-5 > div.md\:flex.w-full.items-start > div > a > h3')
        company = company_element.text
        print(company)

        salary_element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div.md\:px-10.py-3.md\:py-4.px-4.bg-white.shadow-sd-12.rounded-sm.mb-5 > div.md\:flex.w-full.items-start > div > div.md\:flex.mt-5 > div:nth-child(1) > div > p.font-semibold.text-14.text-\[\#8B5CF6\]')
        salary = salary_element.text
        print(salary)

        location_element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div.md\:px-10.py-3.md\:py-4.px-4.bg-white.shadow-sd-12.rounded-sm.mb-5 > div.md\:flex.w-full.items-start > div > div.flex.items-start.min-w-\[250px\].mb-4.mb-6 > div > p:nth-child(2)')
        location = location_element.text
        print(location)

        date_element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div.md\:px-10.py-3.md\:py-4.px-4.bg-white.shadow-sd-12.rounded-sm.mb-5 > div.md\:flex.w-full.items-start > div > div.flex.justify-between.w-full > div:nth-child(2) > span > span.font-semibold')
        date = date_element.text
        print(date)  

        block_infor_element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div.flex.flex-col.lg\:flex-row > div.w-full.lg\:w-3\/4.pb-4 > div.jsx-d84db6a84feb175e.px-4.md\:px-10.py-4.bg-white.shadow-sd-12.rounded-sm > div.jsx-d84db6a84feb175e.bg-\[\#F5F3FF\].px-4.pt-5.pb-1.mb-6')
        block_infor = block_infor_element.text
        print(block_infor)

        yeucau_element = driver.find_element(By.CSS_SELECTOR, '#__next > div > main > div > div.flex.flex-col.lg\:flex-row > div.w-full.lg\:w-3\/4.pb-4 > div.jsx-d84db6a84feb175e.px-4.md\:px-10.py-4.bg-white.shadow-sd-12.rounded-sm > div.jsx-d84db6a84feb175e.mb-4.md\:mb-8 > div')
        yeu_cau = yeucau_element.text
        print(yeu_cau)
        information = Information(title, company, salary, location, date, block_infor, yeu_cau, link_pages[i])
        with open('data_vieclam24h.txt', 'a', encoding='utf8') as file:
            file.write(information.title + "#" + "\n")
            file.write(information.company + "#" + "\n")
            file.write(information.salary+ "#"  + "\n")
            file.write(information.location+ "#"  + "\n")
            file.write(information.date+ "#"  + "\n")
            file.write(information.block_infor+ "#"  + "\n")
            file.write(information.yeu_cau+ "#"  + "\n")
            file.write(information.link+ "#"  + "\n")
    except Exception as e:
        print("BO QUA PAGE " + str(i+1))
        with open('bad_links2_vieclam24h.txt', 'a') as file:
            file.write(link_pages[i] + "\n")
    










# driver.get('https://vieclam24h.vn/xuat-ban-in-an/quan-ly-viet-va-bien-tap-c52p92id200273851.html')
















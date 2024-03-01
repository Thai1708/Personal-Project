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
    def __init__(self, title, company, salary, location, date, cap, nganh_nghe, kinh_nghiem, hinh_thuc, yeu_cau, khac , link):
        self.title = title
        self.company = company
        self.salary = salary
        self.location = location
        self.date = date
        self.cap = cap
        self.nganh_nghe = nganh_nghe
        self.kinh_nghiem = kinh_nghiem
        self.hinh_thuc = hinh_thuc
        self.yeu_cau = yeu_cau
        self.khac = khac
        self.link = link
#--------------------------------------Tao bien link tat ca trang-------------------------------------
with open('link_subpage_cb.txt', 'r', encoding='utf8') as file:
    link_pages = file.read().splitlines()

print(link_pages)

titles = []
companys = []
salarys = []
locations = []      
dates = []
caps = []
nganh_nghes = []
kinh_nghiems = []
hinh_thucs = []
yeu_caus = []
khacs = []

bad_links = []
for i in range(2050, len(link_pages)):
    print('DANG O TRANG ', str(i+1))
    driver.get(link_pages[i])
    sleep(1)
    try:
        login_button = driver.find_element(By.CSS_SELECTOR, 'body > header > div.col-12.alertOnTopSite > span > a')
        login_button.click()
    except Exception as e:
        pass
    try:
        #-----------------------------------------------Trich text can thiet----------------------------------
        title_element = driver.find_element(By.CSS_SELECTOR, 'body > main > section.search-result-list-detail.template-2 > div > div > div.col-12.mb-15 > section > div.apply-now-content > div.job-desc > h1')
        title = title_element.text
        print(title_element.text)

        company_element = driver.find_element(By.CSS_SELECTOR, 'body > main > section.search-result-list-detail.template-2 > div > div > div.col-12.mb-15 > section > div.apply-now-content > div.job-desc > a')
        company = company_element.text
        print(company_element.text)

        salary_element = driver.find_element(By.CSS_SELECTOR, '#tab-1 > section > div.bg-blue > div > div:nth-child(3) > div > ul > li:nth-child(1) > p')
        salary = salary_element.text
        print(salary_element.text)

        location_element = driver.find_element(By.CSS_SELECTOR, '#tab-1 > section > div.bg-blue > div > div:nth-child(1) > div > div > p > a')
        location = location_element.text
        print(location_element.text)

        date_element = driver.find_element(By.CSS_SELECTOR, '#tab-1 > section > div.bg-blue > div > div:nth-child(2) > div > ul > li:nth-child(1) > p')
        date = date_element.text
        print(date_element.text)

        nganh_nghe_element = driver.find_element(By.CSS_SELECTOR, '#tab-1 > section > div.bg-blue > div > div:nth-child(2) > div > ul > li:nth-child(2) > p')
        nganh_nghe = nganh_nghe_element.text
        print(nganh_nghe_element.text)

        kinhnghiem_element = driver.find_element(By.CSS_SELECTOR, '#tab-1 > section > div.bg-blue > div > div:nth-child(3) > div > ul > li:nth-child(2) > p')
        kinh_nghiem = kinhnghiem_element.text
        print(kinhnghiem_element.text)

        cap_element = driver.find_element(By.CSS_SELECTOR, '#tab-1 > section > div.bg-blue > div > div:nth-child(3) > div > ul > li:nth-child(3) > p')
        cap = cap_element.text
        print(cap_element.text)

        hinhthuc_element = driver.find_element(By.CSS_SELECTOR, '#tab-1 > section > div.bg-blue > div > div:nth-child(2) > div > ul > li:nth-child(3) > p')
        hinh_thuc = hinhthuc_element.text
        print(hinhthuc_element.text)

        yeu_cau_element = driver.find_element(By.XPATH, '//*[@id="tab-1"]/section/div[4]')
        yeu_cau = yeu_cau_element.text
        print(yeu_cau_element.text)


        khac_element = driver.find_element(By.XPATH, '//*[@id="tab-1"]/section/div[5]/div')
        khac = khac_element.text
        print(khac_element.text)
        information = Information(title, company, salary, location, date, cap, nganh_nghe, kinh_nghiem, hinh_thuc, yeu_cau, khac, link_pages[i])
        with open('data_carreerbuilder_1.txt', 'a', encoding='utf8') as file:
            file.write(information.title + "#" + "\n")
            file.write(information.company + "#" + "\n")
            file.write(information.salary+ "#"  + "\n")
            file.write(information.location+ "#"  + "\n")
            file.write(information.date+ "#"  + "\n")
            file.write(information.cap+ "#"  + "\n")
            file.write(information.nganh_nghe+ "#"  + "\n")
            file.write(information.kinh_nghiem+ "#"  + "\n")
            file.write(information.hinh_thuc+ "#"  + "\n")
            file.write(information.yeu_cau+ "#"  + "\n")
            file.write(information.khac+ "#"  + "\n")
            file.write(information.link+ "#"  + "\n")
    except Exception as e:
        print("BO QUA PAGE " + str(i+1))
        with open('bad_links_1.txt', 'a') as file:
            file.write(link_pages[i] + "\n")

sleep(100)
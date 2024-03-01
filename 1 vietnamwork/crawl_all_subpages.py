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


# class Information:
#     def __init__(self, titles, companys, salarys, locations, dates, caps, nganh_nghes, ky_nangs, links):
#         self.titles = titles
#         self.companys = companys
#         self.salarys = salarys
#         self.locations = locations
#         self.dates = dates
#         self.caps = caps
#         self.nganh_nghes = nganh_nghes
#         self.ky_nangs = ky_nangs
#         self.link_pages = link_pages

class Information:
    def __init__(self, title, company, salary, location, date, cap, nganh_nghe, ky_nang, link):
        self.title = title
        self.company = company
        self.salary = salary
        self.location = location
        self.date = date
        self.cap = cap
        self.nganh_nghe = nganh_nghe
        self.ky_nang = ky_nang
        self.link = link

#-----------------------------------------------Link pages-----------------------------------------------
with open('link_nghiencuuvaphantichthitruong.txt', 'r', encoding='utf8') as file:
    link_pages = file.read().splitlines()

# Bat dau tu link 98 trong link.txt
# link_pages = link_pages[97:]

titles = []
companys = []
salarys = []
locations = []      
dates = []
caps = []
nganh_nghes = []
ky_nangs = [] 

for i in range(len(link_pages)):
    print('DANG O TRANG ', str(i+1))
    driver.get(link_pages[i])
    try:
        ad = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-xs-12.btn-wowcv > div > div > div.sc-gSbCxx.fHZxft > div.sc-eWRdud.dGBIml > div.sc-HYMd.hfdlmW > span > svg > path')))
        ad.click()
    except Exception as e:
        print(f"Error: {e}")
    try:
        title_company = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > h1')
    except Exception as e:
        title_company = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail > div.container-fluid.page-foreground > section.page-job-detail__header.page-job-detail__header__have-banner > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > h1')
    #wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > h1
    #wrapper > div.page-job-detail > div.container-fluid.page-foreground > section.page-job-detail__header.page-job-detail__header__have-banner > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > h1
    #wrapper > div.page-job-detail > div.container-fluid.page-foreground > section.page-job-detail__header.page-job-detail__header__have-banner > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > h1
    #wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > h1
    title_company_list = title_company.text.split('\n')
    title = title_company_list[0]
    company = title_company_list[1]
    print('------------------------')
    print(title)
    print(company)
    print('------------------------')
    # titles.append(title)
    # companys.append(company)

    print('******************************')
    try:
        location = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > div:nth-child(2) > div > span > a')
    except Exception as e:
        location = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail > div.container-fluid.page-foreground > section.page-job-detail__header.page-job-detail__header__have-banner > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > div:nth-child(2) > div > span > a')
    
    #wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > div:nth-child(2) > div > span > a
    print(location.text)
    location = location.get_attribute('outerHTML')
    # locations.append(location.text)
    print('******************************')

    print("###################################")
    try:
        salary = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > div:nth-child(3) > div > span.salary > strong')
    except Exception as e:
        salary = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail > div.container-fluid.page-foreground > section.page-job-detail__header.page-job-detail__header__have-banner > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > div:nth-child(3) > div > span.salary > strong')
    print(salary.text)
    salary = salary.get_attribute('outerHTML')
    # salarys.append(salary.text)
    print("###################################")

    date = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(1) > div.col-xs-10.summary-content > span.content')
    print(date.get_attribute('outerHTML'))
    date = date.get_attribute('outerHTML')
    # dates.append(date.get_attribute('outerHTML'))
    #job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(1) > div.col-xs-10.summary-content > span.content

    cap = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(2) > div.col-xs-10.summary-content > span.content')
    print(cap.get_attribute('outerHTML'))
    cap = cap.get_attribute('outerHTML')
    # caps.append(cap.get_attribute('outerHTML'))

    
    nganh_nghe = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(3) > div.col-xs-10.summary-content > span.content > a:nth-child(1)')
    print(nganh_nghe.get_attribute('outerHTML'))
    nganh_nghe = nganh_nghe.get_attribute('outerHTML')
    # nganh_nghes.append(nganh_nghe.get_attribute('outerHTML'))

    ky_nang = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(5) > div.col-xs-10.summary-content > span.content')
    print(ky_nang.get_attribute('outerHTML'))
    ky_nang = ky_nang.get_attribute('outerHTML')
    # ky_nangs.append(ky_nang.get_attribute('outerHTML'))

    information = Information(title, company, salary, location, date, cap, nganh_nghe, ky_nang, link_pages[i])
    with open('data_nghiencuuvaphantichthitruong.txt', 'a', encoding='utf8') as file:
        file.write(information.title + "\n")
        file.write(information.company + "\n")
        file.write(information.salary + "\n")
        file.write(information.location + "\n")
        file.write(information.date + "\n")
        file.write(information.cap + "\n")
        file.write(information.nganh_nghe + "\n")
        file.write(information.ky_nang + "\n")
        file.write(information.link + "\n")

# with open('data6.txt', 'a', encoding='utf8') as file:
#     for i in range(len(information.link_pages)):
#         file.write(information.titles[i] + "\n")
#         file.write(information.companys[i] + "\n")
#         file.write(information.salarys[i] + "\n")
#         file.write(information.locations[i] + "\n")
#         file.write(information.dates[i] + "\n")
#         file.write(information.caps[i] + "\n")
#         file.write(information.nganh_nghes[i] + "\n")
#         file.write(information.ky_nangs[i] + "\n")
#         file.write(information.link_pages[i] + "\n")



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
link_pages = []
for i in range(7,8):
    link_pages.append(f'https://www.vietnamworks.com/viec-lam?q=tiep-thi&page={i}')

for link_ in link_pages:
    sleep(5)
    driver.get(link_)
    sleep(5)
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
    sleep(10)
        


    titles = []
    title_elements = driver.find_elements(By.XPATH, '//div[@class="sc-kWtpeL kLqfwh"]//a[@target="_blank"]')
    print(len(title_elements))
    for t in title_elements:
        titles.append(t.text)

    links = []
    link_elements = driver.find_elements(By.XPATH, '//div[@class="sc-kWtpeL kLqfwh"]//a[@target="_blank"]')
    print(len(link_elements))
    for t in link_elements:
        links.append(t.get_attribute('href'))
        print(t.get_attribute('href'))

    companys = []
    company_elements = driver.find_elements(By.XPATH, '//div[@class="sc-czkgLR iGyGUC"]//a[@target="_blank"]')
    print(len(company_elements))
    for t in company_elements:
        companys.append(t.text)

    salarys = []
    salary_elements = driver.find_elements(By.XPATH, '//div[@class="sc-dExYaf gemOij"]//span[@class="sc-hTUWRQ jiZiav"]')
    print(len(salary_elements))
    for t in salary_elements:
        salarys.append(t.text)

    locations = []
    location_elements = driver.find_elements(By.XPATH, '//div[@class="sc-dExYaf gemOij"]//span[@class="sc-lizKOf fJuHIq"]')
    print(len(location_elements))
    for t in location_elements:
        locations.append(t.text)

    # link_elements = driver.find_elements(By.XPATH, '//div[@class="sc-czkgLR iGyGUC"]//a[@target="_blank"]')
        
    dates = []
    caps = []
    nganh_nghes = []
    ky_nangs = [] 
    for t in links:
        driver.get(t)
        try:
            ad = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-xs-12.btn-wowcv > div > div > div.sc-gSbCxx.fHZxft > div.sc-eWRdud.dGBIml > div.sc-HYMd.hfdlmW > span > svg > path')))
            ad.click()
        except Exception as e:
            print(f"Error: {e}")
        date = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(1) > div.col-xs-10.summary-content > span.content')
        print(date.get_attribute('outerHTML'))
        dates.append(date.get_attribute('outerHTML'))
        #job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(1) > div.col-xs-10.summary-content > span.content

        cap = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(2) > div.col-xs-10.summary-content > span.content')
        print(cap.get_attribute('outerHTML'))
        caps.append(cap.get_attribute('outerHTML'))

        
        nganh_nghe = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(3) > div.col-xs-10.summary-content > span.content > a:nth-child(1)')
        print(nganh_nghe.get_attribute('outerHTML'))
        nganh_nghes.append(nganh_nghe.get_attribute('outerHTML'))

        ky_nang = driver.find_element(By.CSS_SELECTOR, '#job-info > div > div.col-md-4.col-sm-12.tab-sidebar > div > div.box-summary.link-list > div:nth-child(5) > div.col-xs-10.summary-content > span.content')
        print(ky_nang.get_attribute('outerHTML'))
        ky_nangs.append(ky_nang.get_attribute('outerHTML'))
        
    information = Information(titles, companys, salarys, locations, dates, caps, nganh_nghes, ky_nangs, links)
    with open('data6.txt', 'a', encoding='utf8') as file:
        for i in range(len(information.links)):
            file.write(information.titles[i] + "\n")
            file.write(information.companys[i] + "\n")
            file.write(information.salarys[i] + "\n")
            file.write(information.locations[i] + "\n")
            file.write(information.dates[i] + "\n")
            file.write(information.caps[i] + "\n")
            file.write(information.nganh_nghes[i] + "\n")
            file.write(information.ky_nangs[i] + "\n")
            file.write(information.links[i] + "\n")

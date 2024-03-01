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

driver.get('https://www.vietnamworks.com/cosmetics-marketing-executive-1722415-jv?source=searchResults&searchType=2&placement=1722665&sortBy=date')
try:
    ad = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-xs-12.btn-wowcv > div > div > div.sc-gSbCxx.fHZxft > div.sc-eWRdud.dGBIml > div.sc-HYMd.hfdlmW > span > svg > path')))
    ad.click()
except Exception as e:
    print(f"Error: {e}")

title_company = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > h1')

title_company_list = title_company.text.split('\n')
title = title_company_list[0]
company = title_company_list[1]
print('------------------------')
print(title)
print(company)
print('------------------------')

print('******************************')
location = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > div:nth-child(2) > div > span > a')
print(location.text)
print('******************************')


print("###################################")
salary = driver.find_element(By.CSS_SELECTOR, '#wrapper > div.page-job-detail.page-job-detail_no-background > div.container-fluid.page-foreground > div.wrapper-job-detail-header > section > div > div.row > div.col-md-10.col-content-wrapper > div > div.col-lg-9.col-md-9.col-content > div > div:nth-child(3) > div > span.salary > strong')
print(salary.text)
print("###################################")





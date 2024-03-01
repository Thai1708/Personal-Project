#XPATH LINK
#//h3[@class="h3 tooltip tooltipstered"]//a[@target="_blank"]
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

#-------------------------------------Tao class cho 1 tin tuyen dung------------------------------------
class Information:
    def __init__(self, title, company, salary, location, date, cap, nganh_nghe, kinh_nghiem, hinh_thuc, bang_cap, yeu_cau , link):
        self.title = title
        self.company = company
        self.salary = salary
        self.location = location
        self.date = date
        self.cap = cap
        self.nganh_nghe = nganh_nghe
        self.kinh_nghiem = kinh_nghiem
        self.hinh_thuc = hinh_thuc
        self.bang_cap = bang_cap
        self.yeu_cau = yeu_cau
        self.link = link

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
bang_caps = []

bad_links = []
#-------------------------------------Read Link Page.txt-----------------------------------------------
with open('link_subpage_jobsgo.txt', 'r', encoding='utf8') as file:
    link_pages = file.read().splitlines()

#-------------------------------------Crawl Important Information--------------------------------------
for i in range(len(link_pages)):
    print('DANG O TRANG ', str(i+1))
    driver.get(link_pages[i])
    sleep(1)
    try:
        title_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div.media.stack-media-on-mobile.text-left.content-group.pb-0.mrg-top-10 > div.media-body-2 > h1')
        title = title_element.text
        print(title_element.text)

        # link_element = driver.find_element(By.CSS_SELECTOR, '//h3[@class="h3 tooltip tooltipstered"]//a[@target="_blank"]')
        # print(link_element.get_attribute('href'))

        company_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-4.job-detail-col-2 > div > div > div > div.profile-cover > div.media > div.media-body > h2 > a')
        company = company_element.text
        print(company_element.text)
        # Su dung css selector nay de crawl trang loi
# body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-4.job-detail-col-2 > div > div > div > div:nth-child(2) > div.media-body > h2 > a

        salary_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div.media.stack-media-on-mobile.text-left.content-group.pb-0.mrg-top-10 > div.media-body-2 > ul > li:nth-child(2) > span.saraly.text-bold.text-green')
        salary = salary_element.text
        print(salary_element.text)

        location_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div:nth-child(6) > div > div > div > a:nth-child(2) > small')
        location = location_element.text
        print(location_element.text)

        date_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div.row > div:nth-child(3) > p:nth-child(2)')
        date = date_element.text
        print(date_element.text)

        hinhthuc_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div.row > div:nth-child(1) > p:nth-child(2)')
        hinh_thuc = hinhthuc_element.text
        print(hinhthuc_element.text)

        capbac_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div.row > div:nth-child(2) > p:nth-child(2)')
        cap = capbac_element.text
        print(capbac_element.text)

        nganhnghe_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div:nth-child(7) > div')
        nganh_nghe = nganhnghe_element.text
        print(nganhnghe_element.text)

        kinhnghiem_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div.row > div:nth-child(5) > p:nth-child(2)')
        kinh_nghiem = kinhnghiem_element.text
        print(kinhnghiem_element.text)

        bangcap_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div.row > div:nth-child(4) > p:nth-child(2)')
        bang_cap = bangcap_element.text
        print(bangcap_element.text)

        yeucau_element = driver.find_element(By.CSS_SELECTOR, 'body > section.section.colorgb-single.wrap-1.padd-top-0 > div > div > div > div > div.col-sm-8.pr0.job-detail-col-1 > div > div > div:nth-child(9) > div')
        yeu_cau = yeucau_element.text
        print(yeucau_element.text)

        information = Information(title, company, salary, location, date, cap, nganh_nghe, kinh_nghiem, hinh_thuc, yeu_cau, bang_cap, link_pages[i])
        with open('data_jobsgo.txt', 'a', encoding='utf8') as file:
            file.write(information.title + "#" + "\n")
            file.write(information.company + "#" + "\n")
            file.write(information.salary+ "#"  + "\n")
            file.write(information.location+ "#"  + "\n")
            file.write(information.date+ "#"  + "\n")
            file.write(information.cap+ "#"  + "\n")
            file.write(information.nganh_nghe+ "#"  + "\n")
            file.write(information.kinh_nghiem+ "#"  + "\n")
            file.write(information.hinh_thuc+ "#"  + "\n")
            file.write(information.bang_cap+ "#"  + "\n")
            file.write(information.yeu_cau+ "#"  + "\n")
            file.write(information.link+ "#"  + "\n")
    except Exception as e:
        print("BO QUA PAGE " + str(i+1))
        with open('bad_links_jobsgo.txt', 'a') as file:
            file.write(link_pages[i] + "\n")

sleep(7)

# link_element = driver.find_element(By.CSS_SELECTOR, '//h3[@class="h3 tooltip tooltipstered"]//a[@target="_blank"]')
# for t in link_element:
#     print(t.get_attribute('href'))
#DANG O TRANG  4311
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
    def __init__(self, title, company, salary, location, date, cap, nganh_nghe, kinh_nghiem, hinh_thuc,so_luong, yeu_cau, link):
        self.title = title
        self.company = company
        self.salary = salary
        self.location = location
        self.date = date
        self.cap = cap
        self.nganh_nghe = nganh_nghe
        self.kinh_nghiem = kinh_nghiem
        self.hinh_thuc = hinh_thuc
        self.so_luong = so_luong
        self.yeu_cau = yeu_cau
        self.link = link

################################################################################################
with open('link_subpage_topcv.txt', 'r', encoding='utf8') as file:
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
so_luongs = []
yeu_caus = []

bad_links = []

for i in range(3135, len(link_pages)):
    print("*********************************************************************")
    print('DANG O TRANG ', str(i+1))
    driver.get(link_pages[i])
    sleep(1)
    try:
        close_button = driver.find_element(By.CSS_SELECTOR, '#popup-survey-recruitment-trend > div > div > div.modal-header > button')
        close_button.click()
    except Exception as e:
        print("PAGE khong co quang cao")
    try:
        title_element = driver.find_element(By.CSS_SELECTOR, '#header-job-info > h1')
        print(title_element.text)
        title = title_element.text

        company_element = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__company > div.job-detail__company--information > div.job-detail__company--information-item.company-name > h2 > a')
        print(company_element.text)
        company = company_element.text

        salary_element = driver.find_element(By.CSS_SELECTOR, '#header-job-info > div.job-detail__info--sections > div:nth-child(1) > div.job-detail__info--section-content > div.job-detail__info--section-content-value')
        print(salary_element.text)
        salary = salary_element.text

        location_element = driver.find_element(By.CSS_SELECTOR, '#header-job-info > div.job-detail__info--sections > div:nth-child(2) > div.job-detail__info--section-content > div.job-detail__info--section-content-value')
        print(location_element.text)
        location = location_element.text

        date_element = driver.find_element(By.CSS_SELECTOR, '#header-job-info > div.job-detail__info--deadline')
        print(date_element.text)
        date = date_element.text

        capbac_element = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(1) > div.box-general-group-info > div.box-general-group-info-value')
        print(capbac_element.text)
        cap = capbac_element.text

        kinhnghiem_element = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(2) > div.box-general-group-info > div.box-general-group-info-value')
        print(kinhnghiem_element.text)
        kinh_nghiem = kinhnghiem_element.text

        soluong_element = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(3) > div.box-general-group-info > div.box-general-group-info-value')
        print(soluong_element.text)
        so_luong = soluong_element.text

        hinhthuc_element = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(4) > div.box-general-group-info > div.box-general-group-info-value')
        print(hinhthuc_element.text)
        hinh_thuc = hinhthuc_element.text

        nganh_element = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-category > div:nth-child(1) > div.box-category-tags')
        print(nganh_element.text)
        nganh_nghe = nganh_element.text

        yeu_cau_element = driver.find_element(By.CSS_SELECTOR, '#box-job-information-detail > div.job-detail__information-detail--content > div > div:nth-child(2) > div')
        print(yeu_cau_element.text)
        yeu_cau = yeu_cau_element.text

        information = Information(title, company, salary, location, date, cap, nganh_nghe, kinh_nghiem, hinh_thuc, so_luong, yeu_cau, link_pages[i])
        with open('data_topcv_1.txt', 'a', encoding='utf8') as file:
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
            file.write(information.so_luong+ "#"  + "\n")
            file.write(information.link+ "#"  + "\n")
    except Exception as e:
        print("BO QUA PAGE " + str(i+1))
        with open('bad_links_topcv.txt', 'a') as file:
            file.write(link_pages[i] + "\n")
    


# driver.get('https://www.topcv.vn/viec-lam/nhan-vien-livestream-tiktok-nganh-my-pham-thu-nhap-den-15-trieu-thang-di-lam-ngay/1189567.html?ta_source=JobSearchList_LinkDetail&u_sr_id=4Idcmcl5oLyuL9iHnPGpcP3HJQmgGqkAH2a3rGTD_1703055727')


# sleep(0.5)
# #-----------------------------Trich thong tin quan trong--------------------------------------------


# sleep(100)


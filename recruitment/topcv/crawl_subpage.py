# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import pandas as pd

import os
from time import sleep
import random

# Declare browser

os.environ['PATH'] += r"C:/SeleniumDrivers"
# Khởi tạo trình duyệt Chrome
options = webdriver.ChromeOptions()

# # Tắt notifications
# prefs = {"profile.default_content_setting_values.notifications": 2}
# options.add_experimental_option("prefs", prefs)

# Khởi tạo trình duyệt với các tùy chọn đã thiết lập
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()

# Open URL
driver.maximize_window()
driver.implicitly_wait(2)

driver.get('https://www.topcv.vn/viec-lam/middle-senior-fullstack-developer-lap-trinh-vien-fullstack-tai-ho-chi-minh-thu-nhap-1-000-3-000/1187950.html?ta_source=JobSearchList_LinkDetail&u_sr_id=mhJ5tpnwEdRbDjwajeOt2OIOLiaPK5ZEMnA5nOjn_1702710871')

sleep(2)
try:
    close_right = driver.find_element(By.CSS_SELECTOR, '#anti-scam > div > div > button')
    driver.click()
except Exception as e:
    print("Exception")
sleep(4)
try:
    close_ad = driver.find_element(By.XPATH, '//div[@class="modal-header"]//button[@class="close"]')
    close_ad.click()
except Exception as e:
    print("Exception")

experience = driver.find_element(By.XPATH, '//*[@id="job-detail-info-experience"]/div[2]/div[2]')
print(experience.text)

date = driver.find_element(By.CSS_SELECTOR, '#header-job-info > div.job-detail__info--deadline')
print(date.text)

cap_bac = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(1) > div.box-general-group-info > div.box-general-group-info-value').get_attribute('outerHTML')
cap_bac = str(cap_bac)
list_nganh =  cap_bac.split(">")
clean_nganh = list_nganh[1].replace("</div", "")
print(clean_nganh)



so_luong = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(3) > div.box-general-group-info > div.box-general-group-info-value').get_attribute('outerHTML')
so_luong = str(so_luong)
list_luong =  so_luong.split(">")
clean_luong = list_luong[1].replace("</div", "")
print(clean_luong)

hinh_thuc = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(4) > div.box-general-group-info > div.box-general-group-info-value').get_attribute('outerHTML')
hinh_thuc = str(hinh_thuc)
list_ht =  hinh_thuc.split(">")
clean_ht = list_ht[1].replace("</div", "")
print(clean_ht)

#------------------------------------------------------------Yeu cau ung vien
requirements = []
require_elements = driver.find_elements(By.XPATH, '//*[@id="box-job-information-detail"]/div[1]/div/div[2]/div/p')
for item in require_elements:
    requirements.append(item.get_attribute('outerHTML'))

string_list = [str(element) for element in requirements]

for i in range(len(string_list)):
    cleaned_string_list = [s.replace('</p>', '').replace('<p>', '').replace('\n', '') for s in string_list]

print(cleaned_string_list)

# with open("require.txt", "w") as file:
#     file.write('<>'.join(cleaned_strings))

# tuyens = []
# hts = []
# caps = []
# #-------------------------------------------------------------So luong tuyen
# so_luong_tuyen = driver.find_element(By.XPATH, '//*[@id="job-detail"]/div[3]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]')
# print(so_luong_tuyen.text)
# tuyens.append(so_luong_tuyen.text)

# #-------------------------------------------------------------Hinh thuc
# hinh_thuc = driver.find_element(By.XPATH, '//*[@id="job-detail"]/div[3]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]')
# print(hinh_thuc.text)
# hts.append(hinh_thuc.text)
#------------------------------------------------------------Cap bac
# cap_bac = driver.find_element(By.XPATH, '//*[@id="job-detail"]/div[3]/div/div[2]/div[2]/div/div[1]/div[2]/div[2]')
# print(cap_bac.text)
# caps.append(cap_bac.text)

# dataframe = pd.DataFrame(list(zip(tuyens, hts, caps)), columns=['titles', 'links', 'prices'])
# print(dataframe)

sleep(300)



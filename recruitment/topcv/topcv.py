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
driver.implicitly_wait(10)
# def get_simple_infor(pagelink):

#     driver.get(pagelink)

#     sleep(4)
#     try:
#         close_ad = driver.find_element(By.XPATH, '//div[@class="modal-header"]//button[@class="close"]')
#         close_ad.click()
#     except NoSuchElementException:
#         print("NoSuchElementException")

driver.get("https://www.topcv.vn/tim-viec-lam-it-phan-mem-c10026?sort=top_related&page=2")

sleep(4)
close_ad = driver.find_element(By.XPATH, '//div[@class="modal-header"]//button[@class="close"]')
close_ad.click()


#----------------------------------------Crawl Title
titles = []
title_elements = driver.find_elements(By.XPATH, '//h3[@class="title"]//a[@target="_blank"]/span[@data-toggle="tooltip"]')
for e in title_elements:
    titles.append(e.text)
    print(e.text)


#-----------------------------------------Crawl Salary
salarys = []
salary_elements = driver.find_elements(By.XPATH, '//div[@class="box-right"]/label[@class="title-salary"]')

for s in salary_elements:
    print(s.text)
    salarys.append(s.text)
print(len(salary_elements))


#-----------------------------------------Crawl Company
companys = []
company_elements = driver.find_elements(By.XPATH, '//div[@class="title-block"]//a[@class="company"]/strong')

for c in company_elements:
    print(c.text)
    companys.append(c.text)

#-----------------------------------------Crawl Location
locations = []
location_elements = driver.find_elements(By.XPATH, '//div[@class="label-content"]//label[1]')

for l in location_elements:
    print(l.text)
    locations.append(l.text)

#-------------------------------------------Remain Time
remain_times = []
remain_elements = driver.find_elements(By.XPATH, '//div[@class="label-content"]/label[@class="time"]/strong')

for r in remain_elements:
    print(r.text)
    remain_times.append(r.text)

#------------------------GET LINKPAGE FROM FILE----------------
    
# linkpages = []
# with open('linkpage.txt', 'r') as file:
#     # Đọc từng dòng một
#     line = file.readline()
    
#     # Sử dụng vòng lặp để đọc tất cả các dòng trong file
#     while line:
#         # Xử lý dòng theo ý muốn của bạn
#         # Đọc dòng tiếp theo
#         line = file.readline().strip()
#         linkpages.append(line)

#-------------------------GET ALL PAGE---------------------------
        
# for i in range(5):
#     get_simple_infor(linkpages[i])


#-----------------------------------------Crawl Subtitle link
        
sub_links = []
link_elements = driver.find_elements(By.XPATH, '//h3[@class="title"]//a[@target="_blank"]')
for l in link_elements:
    sub_links.append(str(l.get_attribute('href')))
# for link in link_elements:
#     print(link.get_attribute('href'))


experience_list = []
date_list = []
level_list = []
quantity_list = []
time_type_list = []
requirement_list = []
for link in link_elements:
    print(link)
    
    link.click()
    # driver.get(link)
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
    try:
        new_feature = driver.find_element(By.XPATH, '//div[@class="competitive-rating__content-desktop-wrap"]//button[@class="btn btn-topcv-primary competitive-rating__button btn-confirm-close"]')
    
    # Kiểm tra xem cửa sổ hiện tại có còn mở không
        if len(driver.window_handles) > 1:
            new_feature.click()
        else:
            print("Cửa sổ đã đóng trước khi thực hiện click.")
    except Exception as e:
        print(f'Error: {e}')
    
    #----------------Crawl Subpage---------------------
    

    # sleep(2)
    # try:
    #     close_right = driver.find_element(By.CSS_SELECTOR, '#anti-scam > div > div > button')
    #     driver.click()
    # except Exception as e:
    #     print("Exception")
    # sleep(3)
    # try:
    #     close_ad = driver.find_element(By.XPATH, '//div[@class="modal-header"]//button[@class="close"]')
    #     close_ad.click()
    # except Exception as e:
    #     print("Exception")

    experience = driver.find_element(By.XPATH, '//*[@id="job-detail-info-experience"]/div[2]/div[2]')
    print(experience.text)
    experience_list.append(experience)

    date = driver.find_element(By.CSS_SELECTOR, '#header-job-info > div.job-detail__info--deadline')
    print(date.text)
    date_list.append(date)

    cap_bac = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(1) > div.box-general-group-info > div.box-general-group-info-value').get_attribute('outerHTML')
    cap_bac = str(cap_bac)
    list_nganh =  cap_bac.split(">")
    clean_nganh = list_nganh[1].replace("</div", "")
    print(clean_nganh)
    level_list.append(clean_nganh)

    so_luong = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(3) > div.box-general-group-info > div.box-general-group-info-value').get_attribute('outerHTML')
    so_luong = str(so_luong)
    list_luong =  so_luong.split(">")
    clean_luong = list_luong[1].replace("</div", "")
    print(clean_luong)
    quantity_list.append(clean_luong)

    hinh_thuc = driver.find_element(By.CSS_SELECTOR, '#job-detail > div.job-detail__wrapper > div > div.job-detail__body-right > div.job-detail__box--right.job-detail__body-right--item.job-detail__body-right--box-general > div > div:nth-child(4) > div.box-general-group-info > div.box-general-group-info-value').get_attribute('outerHTML')
    hinh_thuc = str(hinh_thuc)
    list_ht =  hinh_thuc.split(">")
    clean_ht = list_ht[1].replace("</div", "")
    print(clean_ht)
    time_type_list.append(clean_ht)

    requirements = []
    require_elements = driver.find_elements(By.XPATH, '//*[@id="box-job-information-detail"]/div[1]/div/div[2]/div/p')
    for item in require_elements:
        requirements.append(item.get_attribute('outerHTML'))
    string_list = [str(element) for element in requirements]
    for i in range(len(string_list)):
        cleaned_string_list = [s.replace('</p>', '').replace('<p>', '').replace('\n', '') for s in string_list]
    clean_requirement = '*'.join(cleaned_string_list)
    print(clean_requirement)
    requirement_list.append(clean_requirement)

    driver.close()
    driver.switch_to.window(driver.window_handles[0])

driver.switch_to.window(driver.window_handles[0]) 
driver.close() 


# print(requirement_list, quantity_list)
dataframe = pd.DataFrame(list(zip(titles, salarys, companys, locations, experience_list, date_list, level_list, quantity_list, time_type_list, requirement_list, sub_links)), columns=['title', 'salary', 'company', 'location', 'experience', 'date', 'level', 'quantity', 'time type', 'requirement', 'link'])
print(dataframe)
output_file_path = "D:/Selenium/recruitment/topcv/data/demo.xlsx"
dataframe.to_excel(output_file_path)
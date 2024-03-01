from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import os
from time import sleep
import random

# Declare browser

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

# Open URL
driver.get("https://topdev.vn/viec-lam-it?src=topdev.vn&medium=mainmenu")
driver.maximize_window()
driver.implicitly_wait(2)
sleep(5)
  
# Option 1:
# pre_height = driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# count = 1
# while True:
#     print('-----scroll: {} times-----'.format(count))
    
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     sleep(2)
#     new_height = driver.execute_script('return document.body.scrollHeight')
    
#     print('new_height: {}\npre_height: {}'.format(new_height, pre_height))

#     if new_height == pre_height:
#         print("While loop Done!!!")
#         break
    
#     count += 1
#     pre_height = new_height

# Crawl data
#----------------------Title
# title_jobs = []
# title_elements = driver.find_elements(By.XPATH, '//div[@class="flex-1"]/h3[@class="line-clamp-1"]/a[1]')
# for title in title_elements:
#     print(title.text)

#-----------------------Company
# companys = []
# company_elements = driver.find_elements(By.XPATH, '//div[@class="mt-1 line-clamp-1"]/a[1]')
# for company in company_elements:
#     print(company.text)

#------------------------Salary
salarys = []
salary_elements = driver.find_elements(By.XPATH, '//div[@class="mt-2 flex items-center justify-start gap-5"]/div[@class="text-primary"]/p')
for e in salary_elements:
    print(e.get_attribute('outerHTML'))
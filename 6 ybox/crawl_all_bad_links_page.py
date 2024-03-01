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
    def __init__(self, all_infor, link):
        self.all_infor = all_infor
        self.link = link

all_infors = []   
links = []

bad_links = []

#-------------------------------------Read Link Page.txt-----------------------------------------------
with open('bad_links_ybox.txt', 'r', encoding='utf8') as file:
    link_pages = file.read().splitlines()

#-------------------------------------Crawl Important Information--------------------------------------
for i in range(len(link_pages)):
    print('DANG O TRANG ', str(i+1))
    driver.get(link_pages[i])
    sleep(1)

    try:
        all_infor_element = driver.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div.page-container > div > div > div > div.container-fluid.spp__content > div > div > div > div.col-sm-6.col-xs-12 > div > div > div')
        all_infor = all_infor_element.text
        print(all_infor_element.text)

        information = Information(all_infor, link_pages[i])
        with open('data_bad_links_ybox.txt', 'a', encoding='utf8') as file:
            file.write(information.all_infor + "#" + "\n")
            file.write(information.link+ "#html"  + "\n")
    except Exception as e:
        print("BO QUA PAGE " + str(i+1))
        with open('bad_links1_ybox.txt', 'a') as file:
            file.write(link_pages[i] + "\n")

# #post-content > div:nth-child(2) > div:nth-child(4)
# #post-content > div:nth-child(2) > div:nth-child(4)




# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# import os
# from time import sleep
# import random

# import pandas as pd
# import numpy as np

# # Declare browser

# os.environ['PATH'] += r"C:/SeleniumDrivers"
# # Khởi tạo trình duyệt Chrome
# options = uc.ChromeOptions()

# # Tắt notifications
# prefs = {"profile.default_content_setting_values.notifications": 2}
# options.add_experimental_option("prefs", prefs)

# # Khởi tạo trình duyệt với các tùy chọn đã thiết lập
# driver = uc.Chrome(options=options)
# # driver = webdriver.Chrome()

# # Open URL
# driver.maximize_window()
# driver.implicitly_wait(3)

# #app > div > div:nth-child(2) > div.page-container > div > div > div > div.container-fluid.spp__content > div > div > div > div.col-sm-6.col-xs-12 > div > div > div


# driver.get('https://ybox.vn/tuyen-dung/hn-ngan-hang-tmcp-dong-nam-a-seabank-tuyen-dung-thuc-tap-sinh-truyen-thong-full-time-2023-658170c82b9221123e201486')
# all_infor = driver.find_element(By.CSS_SELECTOR, '#app > div > div:nth-child(2) > div.page-container > div > div > div > div.container-fluid.spp__content > div > div > div > div.col-sm-6.col-xs-12 > div > div > div')

# print(all_infor.text)

# sleep(10)
# link_mainpages = []

# #Bat dau tu trang thu 2
# for i in range(600):
#     link_mainpage = f"https://vn.indeed.com/jobs?q=marketing&start={(i+1)}0"
#     link_mainpages.append(link_mainpage)
# for link in link_mainpages:
#     print(link)

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

driver.get("https://vn.indeed.com/jobs?q=marketing&start=3810&vjk=18d047ba2f6fa383")
raw_infor_element = driver.find_element(By.CSS_SELECTOR, '#jobsearch-ViewjobPaneWrapper > div > div > div > div.jobsearch-embeddedBody.css-1omm75o.eu4oa1w0 > div > div.jobsearch-JobComponent-description.css-10ybyod.eu4oa1w0')
print(raw_infor_element.text)
sleep(10)


#jobsearch-ViewjobPaneWrapper > div > div > div > div.jobsearch-embeddedBody.css-1omm75o.eu4oa1w0 > div > div.jobsearch-JobComponent-description.css-10ybyod.eu4oa1w0
#jobsearch-ViewjobPaneWrapper > div > div > div > div.jobsearch-embeddedBody.css-1omm75o.eu4oa1w0 > div > div.jobsearch-JobComponent-description.css-10ybyod.eu4oa1w0
#jobsearch-ViewjobPaneWrapper > div > div > div > div.jobsearch-embeddedBody.css-1omm75o.eu4oa1w0 > div > div.jobsearch-JobComponent-description.css-10ybyod.eu4oa1w0

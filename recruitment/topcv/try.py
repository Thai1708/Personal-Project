from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import os
import time
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get('https://www.topcv.vn/viec-lam/support-engineer-scem/1180955.html?ta_source=JobSearchList_LinkDetail&u_sr_id=mhJ5tpnwEdRbDjwajeOt2OIOLiaPK5ZEMnA5nOjn_1702692839')

driver.implicitly_wait(0.5)

time.sleep(4)
close_ad = driver.find_element(By.XPATH, '//div[@class="modal-header"]//button[@class="close"]')
close_ad.click()

hinh_thuc = driver.find_element(By.XPATH, '//div[@class="box-general-group-info"]//div[@class="box-general-group-info-value"]')
print(hinh_thuc.text)


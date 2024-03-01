from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import os
import time
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://www.lazada.vn/dien-thoai-di-dong/?spm=a2o4n.home-vn.6598063730.1.3c663bdczjZ8pA")

driver.implicitly_wait(0.5)

title_elements = driver.find_elements(By.CLASS_NAME, 'RfADt')
#------------------------Title and Link----------
elems = driver.find_elements(By.XPATH, '//div[@class = "RfADt"]/a')
titles = []
links = []
# elems = driver.find_elements(By.CSS_SELECTOR, '.RfADt [href]')
for elem in elems:
    titles.append(elem.text)
for elem in elems:
    links.append(elem.get_attribute('href'))

#--------------------------Price
prices = []
price_elements = driver.find_elements(By.XPATH, '//div[@class="aBrP0"]/span[@class="ooOxS"]')
for price in price_elements:
    prices.append(price.text)

# #-------------------------Aggreate to data frame
dataframe = pd.DataFrame(list(zip(titles, links, prices)), columns=['titles', 'links', 'prices'])
dataframe['index'] = np.arange(1, len(dataframe)+1)
order = ['index', 'titles', 'links', 'prices']
dataframe = dataframe[order]
print(dataframe)

#----------------------------Discount
# discounts = []
# for i in range(1, len(dataframe)+1):
#     try:
#         discount_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[4]/span[1]')
#         discounts.append(discount_element.text)
#     except NoSuchElementException:
#         print(f'NoSuchElementException {i}')

# dataframe['discount'] = pd.DataFrame(discounts)

# print(dataframe)

#------------------------------Location
# sell_products = []
# sell_elements = driver.find_elements(By.XPATH, '//div[@class="_6uN7R"]/span[@class="_1cEkb"]/span[1]')
# for i in range(1, len(dataframe)+1):
#     try:
#         sell_element = driver.find_element(By.XPATH, f'/html/body/div[3]/div/div[3]/div[1]/div/div[1]/div[2]/div[{i}]/div/div/div[2]/div[5]/span[1]/span[1]')
#         sell_products.append(sell_element.text)
#     except NoSuchElementException:
#         print('NoSuchElementException{}'.format(i))

# --------------------------------------Get more product infor








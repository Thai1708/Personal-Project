import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.get("https://www.booking.com/index.vi.html?label=gen173nr-1BCAEoggI46AdIM1gEaPQBiAEBmAEquAEXyAEM2AEB6AEBiAIBqAIDuALhoOKrBsACAdICJDRmOTU3NGQzLTI2MzYtNDVkYS1hZjdiLWM5Yjk1NGFkN2E3MNgCBeACAQ&sid=30d01b6e897492457a9feba14951c033&keep_landing=1&sb_price_type=total&auth_success=1&account_created=1")
driver.implicitly_wait(10)

# driver.implicitly_wait(20)
# my_element = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]')
# my_element.click()
time.sleep(6)
my_element = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Bỏ qua phần đăng nhập."]')
my_element.click()

selection_element = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
selection_element.click()

# people_element = driver.find_element(By.ID, ':rf:')
# // du khac biet
# decrease_element = driver.find_element(By.XPATH, '//div[@id=":rf:"]/div[1]/div[1]/div[2]/button[1]')
# print(adult_element.get_attribute('outerHTML'))
# decrease_element.click()

# increase_element = driver.find_element(By.XPATH, '//div[@id=":rf:"]/div[1]/div[1]/div[2]/button[2]')
# print(adult_element.get_attribute('outerHTML'))
# increase_element.click()



person_number = driver.find_element(By.ID, 'group_adults')
print(person_number.get_attribute('value'))


time.sleep(1)


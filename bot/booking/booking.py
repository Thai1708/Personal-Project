import types
import typing
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from booking import constant as cons
import os

class Booking(webdriver.Chrome):
    def __init__(self, driver_path = r"C:\SeleniumDrivers", teardown = False):
        super().__init__()
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        self.implicitly_wait(15)
        self.maximize_window()
    
    def __exit__(self, exc_type, exc_value, traceback):
    # Code xử lý khi thoát khỏi ngữ cảnh
        if self.teardown:
            self.quit()
        

    def land_first_page(self):
        self.get(cons.BASE_URL)

    def change_currency(self):
        my_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Bỏ qua phần đăng nhập."]')
        my_element.click()
        currency_element = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Giá hiển thị bằng Đồng Việt Nam"]')
        currency_element.click()

        vnd_element = self.find_element(By.XPATH, '//button/div/div/span[text() = "Đô la Mỹ"]')
        vnd_element.click()
    
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, ':re:')
        search_field.clear()
        search_field.send_keys(place_to_go)

        first_result = self.find_element(By.ID, 'autocomplete-result-0')
        first_result.click()
    
    def select_dates(self, check_in_date, check_out_date):
        in_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        in_element.click()
        out_element = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')
        out_element.click()
    
    def select_adults(self, count = 1):
        selection_element = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        selection_element.click()

        while True:
            decrease_element = self.find_element(By.XPATH, '//div[@id=":rf:"]/div[1]/div[1]/div[2]/button[1]')
            decrease_element.click()

            person_number_element = self.find_element(By.ID, 'group_adults')
            person_number = person_number_element.get_attribute('value')
            if int(person_number) == 1:
                break

        increase_element = self.find_element(By.XPATH, '//div[@id=":rf:"]/div[1]/div[1]/div[2]/button[2]')

        for i in range(count - 1):
            increase_element.click()
            
    
    
    
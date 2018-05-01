# coding:utf-8
import time
from selenium import webdriver

class BaseDriver:
    def get_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        time.sleep(3)
        # driver.get(str)
        time.sleep(3)
        return driver
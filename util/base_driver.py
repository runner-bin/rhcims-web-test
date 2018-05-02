# coding:utf-8
import time
from selenium import webdriver

class BaseDriver:
    def get_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("")
        time.sleep(2)
        return driver
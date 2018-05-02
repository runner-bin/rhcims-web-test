# coding:utf-8
import time
from selenium import webdriver

class BaseDriver:
    def get_driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("http://rhcims.rhinformation.com:8080/RHCIMS_LOGIN.html")
        time.sleep(2)
        return driver
# coding:utf-8
import os
import sys
from selenium.webdriver.common.by import By
from selenium import webdriver
from util.method import MultiMethod
from c_login import LoginTest as LT


def loginsuccess(self):
    LT.login_success()

class TabTest():
    def __init__(self):
        self.method = MultiMethod()
        self.driver = webdriver

    @loginsuccess
    def status_tab(self):
        for i in range(2):
            sss = self.driver.find_element_by_css_selector("ul#displayboard>li[i]")
            print sss



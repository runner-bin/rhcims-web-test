# coding:utf-8
import os
import sys
from selenium.webdriver.common.by import By
from selenium import webdriver
from util.method import MultiMethod
from c_login import LoginTest as LT

def loginsuccess(self):
    LT.login_success()

class AlarmTest():
    def __init__(self):
        self.method = MultiMethod()
        self.driver = webdriver

    @loginsuccess
    def history_alarm(self):
        self.driver.find_element_by_css_selector("li#btnHistoryAlm").click()
        self.driver.find_element_by_id("btnBrowseHistoryAlm").click()

    @history_alarm
    def history_alarm_filter_all(self):
        self.driver.find_element_by_css_selector("input#chkEnableFilter").click()

    @history_alarm
    def history_alarm_filter_type(self):
        pass

    @history_alarm
    def history_alarm_filter_type(self):
        pass

    @history_alarm
    def history_alarm_filter_level(self):
        pass

    @history_alarm
    def history_alarm_filter_confirm_state(self):
        pass

    @history_alarm
    def history_alarm_filter_recovery_state(self):
        pass

    @history_alarm
    def history_alarm_filter_alarmfrom(self):
        pass

    @history_alarm
    def history_alarm_filter_alarmid(self):
        pass

    @history_alarm
    def history_alarm_filter_time(self):
        pass

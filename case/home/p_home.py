# coding:utf-8
from util.read_init import ReadIni
from util.get_local import GetLocal
from util.base_driver import BaseDriver

# 此类获取页面的元素，返回元素
class HomeTest:
    def __init__(self):
        self.driver = BaseDriver().get_driver()
        self.get_by_local = GetLocal(self.driver)

    def get_change_button(self):
        return self.get_by_local.get_element('home','changebtn')

    def get_password_element(self):
        return self.get_by_local.get_element('login','password')

    def get_loginbutton_element(self):
        return self.get_by_local.get_element('login','submitbutton')

    def get_error_element(self):
        return self.get_by_local.get_element('login', 'errordata')




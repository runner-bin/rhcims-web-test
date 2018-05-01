# coding:utf-8
import os
import sys
path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"../../")
# path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)
print path
from util.read_init import ReadIni
from util.get_local import GetLocal
from util.base_driver import BaseDriver
class LoginTest:
    def __init__(self):
        self.driver = BaseDriver().get_driver()
        self.get_by_local = GetLocal(self.driver)

    def get_username_element(self):
        return self.get_by_local.get_element('login','username')

    def get_password_element(self):
        return self.get_by_local.get_element('login','password')
    
    def get_loginbutton_element(self):
        return self.get_by_local.get_element('login','submitbutton')




# coding:utf-8
import os
import sys
path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"../../")
# path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)
print path
from handle.h_login import LoginHandle

class LoginBussiness:
    def __init__(self,driver):
        self.login_handle = LoginHandle(driver)
    
    def login_pass(self):
        self.login_handle.send_username('admin')
        self.login_handle.send_username('123')
        self.login_handle.click_login_button()

    def login_user_no_exist(self):
        self.login_handle.send_username(u'管理员')
        self.login_handle.send_username('123')
        self.login_handle.click_login_button()

    def login_pw_error(self):
        self.login_handle.send_username(u'admin')
        self.login_handle.send_username('123456')
        self.login_handle.click_login_button()

    
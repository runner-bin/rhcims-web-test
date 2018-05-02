# coding:utf-8
import time
from case.handle.h_login import LoginHandle
# 此类包含页面的业务层
class LoginBussiness:
    def __init__(self):
        self.login_handle = LoginHandle()

    def login_user_no_exist(self):
        self.login_handle.send_username(u'管理员')
        self.login_handle.send_password('123')
        self.login_handle.click_login_button()
        time.sleep(1)

    def login_pw_error(self):
        self.login_handle.send_username('admin')
        self.login_handle.send_password('123456')
        self.login_handle.click_login_button()
        time.sleep(1)

    def login_pass(self):
        self.login_handle.send_username('admin')
        self.login_handle.send_password('123')
        self.login_handle.click_login_button()
        time.sleep(1)

    def login_clear_data(self):
        self.login_handle.clear_username()
        self.login_handle.clear_password()
        time.sleep(1)






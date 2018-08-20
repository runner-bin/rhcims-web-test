# coding:utf-8
import time
from case.login.h_login import LoginHandle
# 此类包含页面的业务层
class LoginBussiness:
    def __init__(self):
        self.login_handle = LoginHandle()

    def blank_data(self):
        self.login_handle.click_login_button()
        time.sleep(1)
        return self.login_handle.get_prompt_data()

    def blank_user_info(self):
        self.login_handle.send_password('123')
        self.login_handle.click_login_button()
        time.sleep(1)
        return self.login_handle.get_prompt_data()

    def blank_pw_info(self):
        self.login_handle.send_username(u'管理员')
        self.login_handle.click_login_button()
        time.sleep(1)
        return self.login_handle.get_prompt_data()


    def login_user_no_exist(self):
        self.login_handle.send_username(u'管理员')
        self.login_handle.send_password('123')
        self.login_handle.click_login_button()
        time.sleep(1)
        return self.login_handle.get_prompt_data()

    def login_pw_error(self):
        self.login_handle.send_username('admin')
        self.login_handle.send_password('123456')
        self.login_handle.click_login_button()
        time.sleep(1)
        return self.login_handle.get_prompt_data()

    def login_pass(self):
        self.login_handle.send_username('admin')
        self.login_handle.send_password('123')
        self.login_handle.click_login_button()
        time.sleep(1)


    def login_input_verify(self):
        self.login_handle.send_username('@!$@!$')
        self.login_handle.send_password('123')
        self.login_handle.click_login_button()
        time.sleep(1)
        return self.login_handle.get_prompt_data()

    def login_clear_data(self):
        self.login_handle.clear_username()
        self.login_handle.clear_password()







# coding:utf-8
from case.login.p_login import LoginTest

# 此类包含对页面中元素的所有操作
class LoginHandle:
    def __init__(self):
        self.login_test = LoginTest()

    def send_username(self,username):
        self.login_test.get_username_element().send_keys(username)

    def send_password(self,pw):
        self.login_test.get_password_element().send_keys(pw)

    def click_login_button(self):
        self.login_test.get_loginbutton_element().click()

    def clear_username(self):
        self.login_test.get_username_element().clear()

    def clear_password(self):
        self.login_test.get_password_element().clear()

    def get_prompt_data(self):
        return self.login_test.get_error_element().text
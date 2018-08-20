# coding:utf-8
from case.home.p_home import HomeTest

# 此类包含对页面中元素的所有操作
class HomeHandle:
    def __init__(self):
        self.home_test = HomeTest()

    def click_change_btn(self,username):
        self.home_test.get_change_button.click()

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
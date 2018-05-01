# coding:utf-8

import os
import sys
path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"../")
sys.path.append(path)
from page.p_login import LoginTest

class LoginHandle:
    def __init__(self):
        self.login_test = LoginTest()

    def send_username(self,username):
        self.login_test.get_username_element().send_keys(username)
    
    def send_password(self,pw):
        self.login_test.get_password_element().send_keys(pw)
    
    def click_login_button(self):
        self.login_test.get_loginbutton_element().click()
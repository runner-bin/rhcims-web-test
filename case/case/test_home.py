# -*- coding: utf-8 -*-
import unittest, inspect, time


from case.home.b_home import HomeBussiness as HB
from case.login.b_login import LoginBussiness as LB

def get_current_function_name():
    return inspect.stack()[1][3]

class MyClass:
    def function_one(self):
        print("%s.%s" % (self.__class__.__name__, get_current_function_name()))

class RHCase(unittest.TestCase):  # 此类为case
    @classmethod
    def setUpClass(cls):
        cls.l_b = LB()
        cls.l_b.login_pass()
        # cls.h_b = HB()

        time.sleep(1)

    def setUp(self):
        pass

    def test_08_click_change_button(self):
        self.h_b.click_change_btn()
        # self.assertEqual(self.l_b.blank_data(), u"用户名或密码不能为空", u"提示字符串错误")

    # def test_02_blank_user_info(self):
    #     self.assertEqual(self.l_b.blank_user_info(), u"用户名或密码不能为空", u"提示字符串错误")
    #
    # def test_03_blank_pw_info(self):
    #     self.assertEqual(self.l_b.blank_pw_info(), u"用户名或密码不能为空", u"提示字符串错误")
    #
    # def test_04_login_user_no_exist(self):
    #     self.assertEqual(self.l_b.login_user_no_exist(), u"用户不存在", u"提示字符串错误")
    #
    # def test_05_login_pw_error(self):
    #     self.assertEqual(self.l_b.login_pw_error(), u"密码错误", u"提示字符串错误")
    #
    # def test_06_login_input_verify(self):
    #     self.assertNotEqual(self.l_b.login_input_verify(), u"用户不存在", u"登陆输入框未对字符做安全验证")
    #
    # def test_07_login_success(self):
    #     self.l_b.login_pass()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.h_b.home_handle.home_test.driver.quit()

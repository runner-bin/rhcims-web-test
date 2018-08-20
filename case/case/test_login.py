# -*- coding: utf-8 -*-
import unittest
from case.login.b_login import LoginBussiness as LB
import inspect


def get_current_function_name():
    return inspect.stack()[1][3]


class MyClass:
    def function_one(self):
        print("%s.%s" % (self.__class__.__name__, get_current_function_name()))


class RHCase(unittest.TestCase):  # 此类为case
    @classmethod
    def setUpClass(cls):
        cls.l_b = LB()

    def setUp(self):
        self.l_b.login_clear_data()

    def test_01_blank_login_info(self):
        self.assertEqual(self.l_b.blank_data(), u"用户名或密码不能为空", u"提示字符串错误")

    def test_02_blank_user_info(self):
        self.assertEqual(self.l_b.blank_user_info(), u"用户名或密码不能为空", u"提示字符串错误")

    def test_03_blank_pw_info(self):
        self.assertEqual(self.l_b.blank_pw_info(), u"用户名或密码不能为空", u"提示字符串错误")

    def test_04_login_user_no_exist(self):
        self.assertEqual(self.l_b.login_user_no_exist(), u"用户不存在", u"提示字符串错误")

    def test_05_login_pw_error(self):
        self.assertEqual(self.l_b.login_pw_error(), u"密码错误", u"提示字符串错误")

    def test_06_login_input_verify(self):
        self.assertNotEqual(self.l_b.login_input_verify(), u"用户不存在", u"登陆输入框未对字符做安全验证")

    def test_07_login_success(self):
        self.l_b.login_pass()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.l_b.login_handle.login_test.driver.quit()

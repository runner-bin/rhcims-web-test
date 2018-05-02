# -*- coding: utf-8 -*-
import unittest
import sys
from case.bussiness.b_login import LoginBussiness as LB
import inspect


def get_current_function_name():
    return inspect.stack()[1][3]
class MyClass:
    def function_one(self):
        print "%s.%s" % (self.__class__.__name__, get_current_function_name())


class RHCase(unittest.TestCase):# 此类为case，组织bussiness
    @classmethod
    def setUpClass(cls):
        cls.l_b=LB()

    def setUp(self):
        self.l_b.login_clear_data()

    def test_01_login_user_no_exist(self):
        self.l_b.login_user_no_exist()

    def test_02_login_success(self):
        self.l_b.login_pass()

    def tearDown(self):
        if not sys.exc_info()[0]:
            strs = "%s.%s" % (self.__class__.__name__, get_current_function_name())
            print strs
            self.l_b.login_handle.login_test.driver.save_screenshot('..//..//result//sc'+strs+'.png')
            print "PASS"
        try:
            self.l_b.login_clear_data()
        except:
            pass


    @classmethod
    def tearDownClass(cls):
        cls.l_b.login_handle.login_test.driver.quit()

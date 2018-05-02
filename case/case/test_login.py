# -*- coding: utf-8 -*-
import unittest
from case.bussiness.b_login import LoginBussiness as LB

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
        try:
            self.l_b.login_clear_data()
        except:
            pass

    @classmethod
    def tearDownClass(cls):
        pass

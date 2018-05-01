# -*- coding: utf-8 -*-
import unittest
import time
import os
import sys
from datetime import datetime

path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(path)

from HTMLTestRunner import  HTMLTestRunner
from case.bussiness.b_login import LoginBussiness as LB

date = datetime.now().strftime("%Y%m%d")

class RHCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ">start"

    def setUp(self):
        print ">>>>>>start"

    def test_login_success(self):
        self.l_b=LB()
        self.l_b.login_pass()

    def tearDown(self):
        print ">>>>>>end"
    @classmethod
    def tearDownClass(cls):
        print ">end up"


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(RHCase("test_login_success"))
    report_file = path+"//result//"+date+"Report.html"
    fp = file(report_file,"w")
    HTMLTestRunner(fp,verbosity=2).run(suite)

